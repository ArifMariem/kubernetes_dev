from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.models import Operateur

# Update the MySQL connection string with your MySQL database details
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://myuser:mypassword@localhost/mydatabase"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class OperateurRepository:
    def __init__(self, session):
        self.session = session

    def get_operateur_by_id(self, operateur_id: int) -> Operateur:
        query = self.session.query(Operateur).filter_by(idOperateur=operateur_id)
        actual_first_result = query.first()
        print(actual_first_result)   # This should now print the Operateur object
        return actual_first_result


    def create_operateur(self, operateur: Operateur) -> Operateur:
        self.session.add(operateur)
        self.session.commit()
        self.session.refresh(operateur)
        return operateur

