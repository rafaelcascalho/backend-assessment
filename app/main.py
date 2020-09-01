from fastapi import FastAPI, status, HTTPException
import schemas
import services
from ioc import IOC
from dotenv import load_dotenv
from kafka import KafkaProducer


load_dotenv()
app = FastAPI()

# Setup the IOC
ioc = IOC()
ioc.create_context()


@app.get('/health')
def get_health():
    return { "status": "UP" }


@app.post('/login')
def login(user: schemas.User):
    try:
        token = services.login(user.email, user.password, ioc)
        return { "token": token }, status.HTTP_200_OK
    except Exception as exception:
        exception_name = exception.args[0]
        if exception_name == 'NotFound':
            raise HTTPException(status_code=404, detail='User not found')
        elif exception_name == 'InvalidCredentials':
            raise HTTPException(status_code=401, detail='Unauthorized')
        else:
            raise HTTPException(status_code=500, detail='Server internal error')


@app.post('/users')
def create_user(user: schemas.NewUser):
    try:
        user = services.create_user(user, ioc)
        return { "status": "success", "user": user }, status.HTTP_201_CREATED
    except Exception as exception:
        exception_name = exception.args[0]
        if exception_name == 'Conflict':
            raise HTTPException(status_code=409, detail='User already registered')
        else:
            raise HTTPException(status_code=500, detail='Server internal error')


@app.post('/activations/cancel')
def cancel_activation():
    try:
        user = services.create_user(user, ioc)
        return { "status": "success", "user": user }, status.HTTP_201_CREATED
    except Exception as exception:
        raise HTTPException(status_code=500, detail='Server internal error')
