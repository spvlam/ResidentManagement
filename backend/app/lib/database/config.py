from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import Depends

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:lamnv@localhost/RMD"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False}  =>> this line only for SQLite
)
    #each Local session is the database session, class its self is not the database session
    #######################################################
    #######################################################
    #  Database session = connection between app and db   #
    #  ensure the query, error handling,..                #
    #######################################################
    #######################################################
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# base class for create database model
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

RMD_session = Depends(get_db)