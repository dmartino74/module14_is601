from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext

from app.db import get_db
from app.models.base import Base
from app.operations.schemas.user_schemas import UserCreate, UserLogin, UserRead

# --- SQLAlchemy User model ---
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

# --- FastAPI router for user endpoints ---
router = APIRouter(tags=["users"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # bcrypt only supports up to 72 bytes
    encoded = password.encode("utf-8")
    if len(encoded) > 72:
        encoded = encoded[:72]  # truncate safely
    return pwd_context.hash(encoded.decode("utf-8", errors="ignore"))

def verify_password(plain_password: str, hashed_password: str) -> bool:
    encoded = plain_password.encode("utf-8")
    if len(encoded) > 72:
        encoded = encoded[:72]
    return pwd_context.verify(encoded.decode("utf-8", errors="ignore"), hashed_password)

@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_pw = hash_password(user.password)
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": "Login successful", "user_id": db_user.id}
