from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.users import UserRead
from fastapi_users.db import SQLAlchemyBaseUserTable


# class Users(Base):
#     __tablename__ = "users"
#     pydantic_model = UserSchema
    
#     name: Mapped[str]

class User(SQLAlchemyBaseUserTable[int], Base):
    pydantic_model = UserRead
    
    first_name: Mapped[str] = mapped_column(String(length=150), nullable=True)
    last_name: Mapped[str] = mapped_column(String(length=150), nullable=True)
    
    username: Mapped[str] = mapped_column(
        String(length=150), nullable=False, unique=True, index=True
    )
    
    email: Mapped[str] = mapped_column(
            String(length=320), unique=True, index=True, nullable=False
        )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
