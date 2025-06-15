import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"))

def send_sms(to, message):
    return client.messages.create(
        body=message,
        from_=os.getenv("TWILIO_FROM"),
        to=to
    )
