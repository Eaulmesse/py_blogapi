from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session
# from database import engine, SessionLocal

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}