from ioc import IOC
from infra.models import User


def create_user(user: User, ioc: IOC):
    user_repository = ioc.get_repository_for('users')
    created_user = user_repository.save(user)
    return {
        "id": created_user.id,
        "email": created_user.email,
        "role": created_user.role
    }
