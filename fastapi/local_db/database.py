from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
import os

#SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip_address/hostname>/<database_name>"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()