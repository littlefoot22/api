from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ebi(BaseModel):
    ebi_name: str
    target_outcome: str
    pubmed_url: str

AIMS = ebi(ebi_name="Adherence Improving self-Management Strategy", target_outcome="rxadherence", pubmed_url="https://www.ncbi.nlm.nih.gov/pubmed/28262598")
ATHENA = ebi(ebi_name="Adherence Through Home Education and Nursing Assessment", target_outcome="rxadherence", pubmed_url="http://www.ncbi.nlm.nih.gov/pubmed/16770291")


@app.get("/")
async def root():
    return {"message": "Kalamos provides a programmatic interfact for matching, enrolling, and rewarding patients for behavioral health interventions. Our main focus is on communicable diseases, specifically HIV."}


@app.get("/ebi")
async def root():
    return AIMS, ATHENA

@app.post("/ebi")
async def root():
    return {"message": "You do not have permissions to create a new intervention."}

@app.put("/ebi")
async def root():
    return ebis

@app.delete("/ebi")
async def root():
    return {"message": "You do not have permissions to delete an intervention."}

@app.get("/ebi/amvspm")
async def root():
    return {"message": "This is a description of the intervention."}

@app.get("/patient")
async def root():
    return {"message": "return data structure of a patient"}