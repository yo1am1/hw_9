from .models import Number
import os
from twilio.rest import Client

from celery import shared_task


@shared_task
def sending(number):
    account_sid = "ACec2a35c8a53e4f514808e3bfb75bb0b7"
    auth_token = os.getenv("TWILIO_TOKEN")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hello from Twilio", from_="+12707166231", to=number
    )
