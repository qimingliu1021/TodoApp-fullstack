import sys
sys.path.append("..")

from starlette.responses import RedirectResponse

from fastapi import Depends, HTTPException, status, APIRouter, Request, Response, Form
from pydantic import BaseModel
from typing import Optional
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from datetime import datetime, timedelta
from jose import jwt, JWTError

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .auth import get_current_user

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory='templates')

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={401: {"user": "Not authorized"}}
)

class UserInfo: 
  username: str
  old_password: str
  new_password: str

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/change-password", response_class=HTMLResponse)
async def reach_change_password_page(request: Request): 
  return templates.TemplateResponse("change-password.html", {"request": request})

@router.post("/change-password", response_class=HTMLResponse)
async def change_password(request: Request, UserInfo, db: Session = Depends(get_db)): 
  user = get_current_user(request)
  print("in the changing function rn...")
  # db.query(models.Users).filter(models.Users.username == username).first()
  user_model = db.query(models.Users).filter(models.Users.username == user.username).first()

  if user_model.username != UserInfo.username or user_model.hashed_password != UserInfo.password: 
    msg = "Wrong username or password input. Please try again."
    return templates.TemplateResponse("change-password.html", {"request": request, "user": user, "msg": msg})
  
  if UserInfo.old_password == UserInfo.new_password: 
    msg = "New password and old cannot be the same."
    return templates.TemplateResponse("change-password.html", {"request": request, "user": user, "msg": msg})
  
  msg = "Password updated"
  user_model.hashed_password = UserInfo.new_password

  db.add(user_model)
  db.commit()

  return templates.TemplateResponse("change-password.html", {"request": request, "user": user, "msg": msg})




