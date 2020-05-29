from typing import List
import csv

# with open('/data/rxadherence.csv', 'r') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        my_list.append(ebi(row[0], row[1], row[2:]))

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

rxadherence = open('data/rxadherence.csv')

class ebi(BaseModel):
    ebi_name: str
    target_outcome: str
    target_pop: str
    pubmed_url: str

AIMS = ebi(ebi_name="Adherence Improving self-Management Strategy", target_outcome="rxadherence", target_pop="HIV clinic patients who are antiretroviral treatment-experienced or treatment naïve", pubmed_url="https://www.ncbi.nlm.nih.gov/pubmed/28262598")

ATHENA = ebi(ebi_name="Adherence Through Home Education and Nursing Assessment", target_outcome="rxadherence", target_pop= "HIV-positive clinic patients who are antiretroviral treatment-experienced", pubmed_url="http://www.ncbi.nlm.nih.gov/pubmed/16770291")

@app.get("/")
async def root():
    return {"message": "Kalamos provides a programmatic interfact for matching, enrolling, and rewarding patients for behavioral health interventions. Our main focus is on communicable diseases, specifically HIV."}

@app.get("/ebi")
async def root():
    return [
        row
        for row in rxadherence
    ]

@app.post("/ebi")
async def root():
    return {"message": "You do not have permissions to create a new intervention."}

@app.put("/ebi")
async def root():
    return ebis

@app.delete("/ebi")
async def root():
    return {"message": "You do not have permissions to delete an intervention."}

@app.get("/clinic")
async def root():
    return {"message": "This should search the npin by zip https://npin.cdc.gov/api/organization/proximity"}

@app.get("/patient")
async def root():
    return {"message": "return data structure of a patient"}