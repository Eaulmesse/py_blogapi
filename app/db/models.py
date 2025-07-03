from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, relationship, Text
from sqlalchemy.sql import func
from .base import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
    
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    content = Column(Text, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now() , server_default=func.now())

    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
