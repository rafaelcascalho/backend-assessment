class User:
    email: str
    password: str
    role: ['external_app', 'customer', 'super_user']


class ExternalApp(User):
    customer_mid: str


class SuperUser(User):
    pass


class Customer(User):
    pass
