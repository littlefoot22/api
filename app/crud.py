from sqlalchemy.orm import Session

import models
import schemas

from pydantic import BaseModel


def get_ebis(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ebi).offset(skip).limit(limit).all()

async def create_user(user: schemas.UserCreate, db: Session):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user