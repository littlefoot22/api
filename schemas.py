from pydantic import BaseModel

class Ebi(BaseModel):
    id: int
    ebi_name: str
    target_outcome: str
    target_pop: str
    pubmed_url: str
​
    class Config:
        orm_mode = True