import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from infra import models
from contextlib import contextmanager
from infra.repositories import UserSQLRepository, TokenRepository


class Database:
    def __init__(self):
        self.metadata = MetaData()
        name = os.getenv("DB_NAME")
        user = os.getenv("DB_USER")
        host = os.getenv("DB_HOST")
        password = os.getenv("DB_PASSWORD")
        self.engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{name}')
        models.Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_engine(self):
        return self.engine

    def get_metadata(self):
        return self.metadata

    def session_local(self):
        return self.session_local

    @contextmanager
    def transaction(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
