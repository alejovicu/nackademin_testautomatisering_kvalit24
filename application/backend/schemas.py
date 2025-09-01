from pydantic import BaseModel
from typing import List

class ProductBase(BaseModel):
    name: str

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    products: List[ProductResponse] = []
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
