from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Kalamos provides a programmatic interfact for matching, enrolling, and rewarding patients for behavioral health interventions. Our main focus is on communicable diseases, specifically HIV."}


@app.get("/ebi")
async def root():
    return {"message": "This is a list of supported evidence based interventions."}

@app.post("/ebi")
async def root():
    return {"message": "You do not have permissions to create a new intervention."}

@app.put("/ebi")
async def root():
    return {"message": "You do not have permissions to update an intervention."}

@app.delete("/ebi")
async def root():
    return {"message": "You do not have permissions to delete an intervention."}

@app.get("/ebi/amvspm")
async def root():
    return {"message": "This is a description of the intervention."}

