import os
from fastapi_mail import FastMail


templates = {
    "ActivationCancelled": """
    <h1>Thank you for your request!</h1>

    <p>But at this time we are not able to accept it.</p>
    """,

    "ActivationApproved": """
    <h1>Thank you for your request!</h1>

    <p>You now can use credit in out platforme.</p>
    """,
}


async def send_email(email: str, result: str):
    mail = FastMail(
        email=os.getenv('DEFAULT_EMAIL'), 
        password=os.getenv('DEFAULT_EMAIL_PASSWORD'),
        tls=True,
        port="587",
        service="gmail"
    )
    await mail.send_message(
        recipient=email, 
        subject="Activation Request Result",
        body=templates[result],
        text_format="html"
    )
