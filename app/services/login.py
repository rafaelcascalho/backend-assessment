from bcrypt import gensalt, hashpw, checkpw
from jwt import encode
from ioc import IOC

def login(email: str, password: str, ioc: IOC):
    user_repository = ioc.get_repository_for('users')
    token_repository = ioc.get_repository_for('tokens')

    user = user_repository.find_by_email(email)
    if user is None:
        raise Exception('NotFound')
    if checkpw(str.encode(password), str.encode(user.password)):
        raise Exception('InvalidCredentials')

    token = encode({ "sub" : user.id }, 'secret', algorithm='HS512')
    token_repository.save(token)
    return token
