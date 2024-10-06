import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def send_email():
    # Retrieve the SendGrid API key from environment variables
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    if not SENDGRID_API_KEY:
        logging.error("SendGrid API key not set in environment variables.")
        return

    # Define email parameters
    from_email = Email(os.environ.get('FROM_EMAIL'))  # Verified sender email
    to_email = To(os.environ.get('TO_EMAIL'))         # Recipient email address
    subject = "Hourly Reminder"
    content = Content("text/plain", "This is your hourly reminder to stay focused and productive!")

    # Create a Mail object
    mail = Mail(from_email, to_email, subject, content)

    # Create a SendGrid client
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

    try:
        # Send the email
        response = sg.send(mail)
        logging.info(f"Email sent! Status Code: {response.status_code}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    send_email()
