from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import UserCreate, UserResponse
from app.db.sql_database import get_db
from app.core.config import settings
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if settings.DATABASE_TYPE == "sql":
        from app.models.sql_models import User
        from passlib.context import CryptContext
        
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        
        db_user = db.query(User).filter(User.email == user.email).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        hashed_password = pwd_context.hash(user.password)
        new_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    elif settings.DATABASE_TYPE == "cassandra":
        from app.db.cassandra_database import get_cassandra_session
        session = get_cassandra_session()
        
        user_id = uuid.uuid4()
        session.execute(
            """
            INSERT INTO users (id, username, email, created_at)
            VALUES (%s, %s, %s, %s)
            """,
            (user_id, user.username, user.email, datetime.now())
        )
        return UserResponse(
            id=str(user_id),
            username=user.username,
            email=user.email,
            created_at=datetime.now()
        )

@router.get("/", response_model=List[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    if settings.DATABASE_TYPE == "sql":
        from app.models.sql_models import User
        users = db.query(User).all()
        return users
    
    elif settings.DATABASE_TYPE == "cassandra":
        from app.db.cassandra_database import get_cassandra_session
        session = get_cassandra_session()
        
        rows = session.execute("SELECT * FROM users")
        users = []
        for row in rows:
            users.append(UserResponse(
                id=str(row.id),
                username=row.username,
                email=row.email,
                created_at=row.created_at
            ))
        return users

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str, db: Session = Depends(get_db)):
    if settings.DATABASE_TYPE == "sql":
        from app.models.sql_models import User
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    elif settings.DATABASE_TYPE == "cassandra":
        from app.db.cassandra_database import get_cassandra_session
        session = get_cassandra_session()
        
        row = session.execute(
            "SELECT * FROM users WHERE id = %s",
            (uuid.UUID(user_id),)
        ).one()
        
        if not row:
            raise HTTPException(status_code=404, detail="User not found")
        
        return UserResponse(
            id=str(row.id),
            username=row.username,
            email=row.email,
            created_at=row.created_at
        )
