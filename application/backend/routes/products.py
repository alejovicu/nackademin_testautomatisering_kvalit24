from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
from schemas import ProductCreate, ProductResponse
from models import Product, User
from typing import List

ADMIN_USER_ID = 1

router = APIRouter()

def validate_admin_user(user_id):
    if user_id != ADMIN_USER_ID:
        raise HTTPException(
            status_code=403,
            detail="The user doesn't have permissions. Only the Admin user can manage products from the catalog."
        )

@router.post("/product", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    validate_admin_user(current_user.id)

    # Fail if product with the same name already exists
    existing_product = db.query(Product).filter(Product.name == product.name).first()
    if existing_product:
        raise HTTPException(
            status_code=409,
            detail=f"A product with the name [{product.name}] already exists.",
        )
    
    # Add new product
    new_product = Product(name=product.name)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.get("/products", response_model=List[ProductResponse])
def list_products(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(Product).all()


@router.delete("/product/{product_id}", response_model=ProductResponse)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    validate_admin_user(current_user.id)

    # Fail if the product doesn't exist
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
