from sqlalchemy.orm import Session

import models
import schemas


def get_ebis(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ebi).offset(skip).limit(limit).all()
