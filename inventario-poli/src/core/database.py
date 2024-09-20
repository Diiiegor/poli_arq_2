from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# database variables
database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
database_host = os.getenv('DATABASE_HOST')
database_port = os.getenv('DATABASE_PORT')
database_schema = os.getenv('DATABASE_SCHEMA')
database_url = f"postgresql://{database_user}:{database_password}@{database_host}:{database_port}/{database_schema}"
engine = create_engine(database_url,connect_args={"options": f"-csearch_path={database_schema}"})
db_session = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
