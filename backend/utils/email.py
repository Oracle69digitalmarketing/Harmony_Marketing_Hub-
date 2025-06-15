import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_FROM = os.getenv("EMAIL_FROM")
FRONTEND_URL = os.getenv("FRONTEND_URL")

def send_verification_email(to_email: str, token: str):
    verify_link = f"{FRONTEND_URL}/verify?token={token}"
    subject = "Verify Your Harmony Marketing Hub Account"
    body = f"""
Hi there,

Please click the link below to verify your Harmony Marketing Hub account:

{verify_link}

If you didn't sign up, ignore this email.

— Harmony Team
"""

    message = Mail(
        from_email=EMAIL_FROM,
        to_emails=to_email,
        subject=subject,
        plain_text_content=body
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
    except Exception as e:
        print("[SendGrid Error]", e)
