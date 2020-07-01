from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base

class Ebi(Base):
    __tablename__ = "ebis"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    target_outcome = Column(String)
    target_pop = Column(String)
    pubmed_url = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
