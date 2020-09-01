import os
import abc
from sqlalchemy import create_engine, MetaData
from infra import models
from infra.repositories import UserSQLRepository, TokenRepository
from infra.database import Database


class IOC:
    def __init__(self):
        self.context = {}

    def create_context(self):
        db = Database()
        metadata = db.get_metadata()
        engine = db.get_engine()

        user_repository = UserSQLRepository(metadata, engine, db.transaction)
        token_repository = TokenRepository()

        self.context['users'] = user_repository
        self.context['tokens'] = token_repository

    def get_repository_for(self, name):
        return self.context[name]
