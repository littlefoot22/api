from sqlalchemy.orm import Session

import models
import schemas
import bcrypt

from pydantic import BaseModel


def get_ebis(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ebi).offset(skip).limit(limit).all()

async def create_user(user: schemas.UserCreate, db: Session):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def create_user(user: schemas.UserCreate, db: Session):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def check_password(user: schemas.UserLogin, db: Session):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    
    #Load hashed from the db and check the provided password
    if bcrypt.hashpw(user.password.encode('utf-8'), db_user.hashed_password) == db_user.hashed_password:
        print("MATCH LOL")
        return "It matches"
    else:
        return "It does not match"