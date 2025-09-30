from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
from schemas import UserResponse
from models import User, Product

router = APIRouter()

@router.get("/user", response_model=UserResponse)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/user/product/{product_id}", response_model=UserResponse)
def assign_product(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product not in current_user.products:
        current_user.products.append(product)
        db.commit()
        db.refresh(current_user)
    return current_user

@router.delete("/user/product/{product_id}", response_model=UserResponse)
def unassign_product(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product in current_user.products:
        current_user.products.remove(product)
        db.commit()
        db.refresh(current_user)
    return current_user
