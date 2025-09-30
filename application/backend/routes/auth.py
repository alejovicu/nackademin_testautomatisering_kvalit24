from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas import UserCreate, UserResponse, Token
from models import User
from auth import get_password_hash, authenticate_user, create_access_token

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):

    # Validate non empty
    if (user.username is None) or (user.username == ""):
       raise HTTPException(status_code=400, detail="Empty username is not allowed")
    if (user.password is None) or (user.password == ""):
       raise HTTPException(status_code=400, detail="Empty password is not allowed")

    # Validate if the user already exist
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")


    hashed_pw = get_password_hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=Token)
def login(form_data: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}
