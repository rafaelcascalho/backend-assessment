import abc


class UsersRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find(self, id: str):
        pass

    @abc.abstractmethod
    def find_by_email(self, email: str):
        pass

    @abc.abstractmethod
    def all(self):
        pass

    @abc.abstractmethod
    def save(self):
        pass
