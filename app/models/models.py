from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Operateur(Base):
    __tablename__ = "operateurs"

    idOperateur = Column(Integer, primary_key=True)
    nom = Column(String)
    prenom = Column(String)
    password= Column(String)
