from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
from schemas import ProductCreate, ProductResponse
from models import Product, User
from typing import List

router = APIRouter()

@router.post("/products", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != 1:
        raise HTTPException(status_code=403, detail="Not allowed")
    new_product = Product(name=product.name)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/products", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Product).all()

@router.delete("/product/{product_id}", response_model=ProductResponse)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != 1:
        raise HTTPException(status_code=403, detail="Not allowed")
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Remove associations with all users
    for user in product.owners:
        user.products.remove(product)

    # Delete the product itself
    db.delete(product)
    db.commit()

    return product
