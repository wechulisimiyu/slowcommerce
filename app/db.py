from sqlmodel import SQLModel, create_engine
from . import models

def create_user():
    user = models.User(username="tanner", email="tanner@hey.mail", full_name="Gary Tanner", password="tanner3232")

sqlite_file_name = "commerce.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()