from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Kalamos provides a programmatic interfact for matching, enrolling, and rewarding patients for behavioral health interventions. Our main focus is on communicable diseases, specifically HIV."}


@app.get("/ebis")
# async def root():
#    return {"message": "hi" }
# async def get_ebis(db: Session, skip: int = 0, limit: int = 10):
# return db.query(models.Ebi).offset(skip).limit(limit).all()
def get_ebis(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ebis = crud.get_ebis(db, skip=skip, limit=limit)
    return ebis

# @app.post("/ebis")
# async def create_ebi():
#   return {"message": "You do not have permissions to create a new intervention."}

# @app.put("/ebis")
# async def update_ebi():
#    return {"message": "You do not have permissions to update an intervention."}

# @app.delete("/ebis")
# async def delete_ebi():
#     raise HTTPException(status_code=403, detail="go away")

# @app.get("/ebi/amvspm")
# async def root():
#    return {"message": "This is a description of the intervention."}

# @app.get("/patient")
# async def root():
#    return {"message": "return data structure of a patient"}

@app.post("/users")
def post_registration(user: schemas.UserCreate, db: Session = Depends(get_db)):
    #db_user = crud.get_user_by_email(db, email=user.email)
    #if db_user:
    #    raise HTTPException(status_code=400, detail="Email already registered")
    crud.create_user(user, db)
    return {"message": "user created"}