from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Operateur

# Update the MySQL connection string with your MySQL database details
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://myuser:mypassword@localhost/mydatabase"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class OperateurRepository:
    def __init__(self):
        self.session = SessionLocal()

    def get_operateur_by_id(self, operateur_id: int) -> Operateur:
        return self.session.query(Operateur).filter(Operateur.idOperateur == operateur_id).first()

    def create_operateur(self, operateur: Operateur) -> Operateur:
        self.session.add(operateur)
        self.session.commit()
        self.session.refresh(operateur)
        return operateur

