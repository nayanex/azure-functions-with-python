# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import logging
import os

import azure.functions as func
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import Config


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(
        "Python HTTP trigger function processed a request to Send an email with Twilio SendGrid."
    )

    message = Mail(
        from_email=Config.FROM_EMAIL,
        to_emails=Config.TO_EMAIL,
        subject="Sending with Twilio SendGrid is Fun",
        html_content="<strong>and easy to do anywhere, even with Python</strong>",
    )

    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return func.HttpResponse("Message successfully sent.")
    except Exception as e:
        print(e.message)
