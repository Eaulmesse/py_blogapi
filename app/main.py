from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session
from core.config import settings
# from database import engine, SessionLocal

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="API pour un blog",
)

@app.get("/")
async def root():
    return {"message": "Hello World"}