from . import models, schemas
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
​
app = FastAPI()
​
@app.get("/")
async def root():
    return {"message": "Kalamos provides a programmatic interfact for matching, enrolling, and rewarding patients for behavioral health interventions. Our main focus is on communicable diseases, specifically HIV."}
​
​
@app.get("/ebis")
async def get_ebis(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Ebi).offset(skip).limit(limit).all()
​
​
@app.post("/ebis")
async def create_ebi():
    return {"message": "You do not have permissions to create a new intervention."}
​
​
@app.put("/ebis")
async def update_ebi():
    return ebis
​
​
# @app.delete("/ebis")
# async def delete_ebi():
#     raise HTTPException(status_code=403, detail="go away")
​
​
@app.get("/ebi/amvspm")
async def root():
    return {"message": "This is a description of the intervention."}
​
​
@app.get("/patient")
async def root():
    return {"message": "return data structure of a patient"}