import abc
from kafka import KafkaConsumer
from msgpack import unpackb


class CommandHandler(metaclass=abc.ABCMeta):
    consumer: KafkaConsumer

    @abc.abstractmethod
    def run(self, message=None):
        pass


class AuthenticationFailed(CommandHandler):
    def __init__(self):
        self.consumer = KafkaConsumer('AuthenticationFailed')

    def run(self, message):
        print(f' ======== Request Authentication Failed! ========')


class AuthenticationCodeIssued(CommandHandler):
    def __init__(self):
        self.consumer = KafkaConsumer('AuthenticationCodeIssued')

    def success(self, payload):
        print(f' ======== Request Authentication Succeded! ======== ')
        print(f'User: {payload.user.email}')
        print(f'GeneratedToken: {payload.token}')
        print('==================================================')


class IssueProductActivation(CommandHandler):
    def __init__(self):
        self.consumer = KafkaConsumer('ActivationSubmitted')

    def run(self, message):
        payload = unpackb(message)
        # do something regarding ActivationRequests


class ActivationCancelled(CommandHandler):
    def __init__(self):
        self.consumer = KafkaConsumer('ActivationCancelled')

    def run(self, message):
        payload = unpackb(message)
        # do something regarding ActivationRequests


class ActivationApproved(CommandHandler):
    def __init__(self):
        self.consumer = KafkaConsumer('ActivationApproved')

    def run(self, message):
        payload = unpackb(message)
        # do something regarding ActivationRequests
