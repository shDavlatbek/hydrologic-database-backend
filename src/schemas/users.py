from typing import Optional
from pydantic import BaseModel, EmailStr, Field

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    first_name: str
    last_name: str
    username: str


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    

# class UserSchema(BaseModel):
#     id: int
    
#     email: EmailStr
#     hashed_password: str
#     is_active: bool
#     is_superuser: bool
#     is_verified: bool

#     class Config:
#         from_attributes = True

# class UserSchemaAdd(BaseModel):
#     name: str
