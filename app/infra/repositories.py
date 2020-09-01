from core.respositories import UsersRepository
from sqlalchemy.orm import Session
from infra.models import User
from bcrypt import gensalt, hashpw


class UserSQLRepository(UsersRepository):
    def __init__(self, metadada, engine, db):
        self.engine = engine
        self.db = db

    def find(self, id: str):
        pass

    def find_by_email(self, email: str):
        with self.db() as db:
            return db.query(User).filter(User.email == email).first()

    def all(self):
        pass

    def save(self, user: User):
        with self.db() as db:
            password_hash = hashpw(str.encode(user.password), gensalt())
            user = User(email=user.email, password=password_hash, role=user.role)
            db.add(user)
            db.commit()
            db.refresh()
            return user


class TokenRepository:
    def __init__(self, *args, **kwargs):
        self.tokens = []

    def find(self, token):
        return True if token in self.tokens else False

    def save(self, token):
        if token in self.tokens:
            raise Exception('TokenAlreadyExists')
        self.tokens.append(token)
