from kafka import KafkaProducer
from msgpack import packb


class Command:
    producer: KafkaProducer

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')


class RequestToken(Command):
    def execute(self, status: str, message: object):
        if status == 'failed':
            self.producer.send('AuthenticationFailed', b'')
        else:
            self.producer.send('AuthenticationCodeIssued', packb(message))


class IssueProductActivation(Command):
    def execute(self, message: object):
        self.producer.send('ActivationSubmitted', packb(message))


class RejectActivation(Command):
    def execute(self, status: str, message: object):
        self.producer.send('ActivationCancelled', packb(message))


class ApproveActivation(Command):
    def execute(self, status: str, message: object):
        self.producer.send('ActivationApproved', packb(message))
