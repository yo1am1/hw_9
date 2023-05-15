from .models import Number
import os
from twilio.rest import Client

from celery import shared_task

TWILIO_ACCOUNT_SID = ''
TWILIO_TOKEN= ''
TWILIO_NUMBER=""
try:
    client=Client(TWILIO_ACCOUNT_SID, TWILIO_TOKEN)
except Exception as e:
    print(f"An error occurred: {str(e)}")


@shared_task
def sending():
    number = Number.objects.last("number")
    message = client.messages.create(from_=TWILIO_NUMBER, to=number)
    return