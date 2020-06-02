from pydantic import BaseModel

class ebi(BaseModel):
    ebi_name: str
    target_outcome: str
    target_pop: str
    pubmed_url: str

ebis = [
    ebi(
        ebi_name="",
        target_outcome="rxadherence",
        target_pop= "",
        pubmed_url=""
    )
    
]