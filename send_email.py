import os
import base64
import json
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

    # Retrieve and decode the recipients data
    encoded_data = os.environ.get('RECIPIENTS_DATA')
    recipients = json.loads(encoded_data)
    if not encoded_data:
        logging.error("Recipients data not set in environment variables.")
        return

    # try:
    #     decoded_data = base64.b64decode(encoded_data).decode('utf-8')
    #     recipients = json.loads(decoded_data)
    # except Exception as e:
    #     logging.error(f"Failed to decode and parse recipients data: {e}")
    #     return

    # Sender email
    from_email = Email(os.environ.get('FROM_EMAIL'))  # Verified sender email
    if not from_email.email:
        logging.error("Sender email not set in environment variables.")
        return

    # Create a SendGrid client
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

    # Send emails to each recipient
    for email, message in recipients.items():
        to_email = To(email)
        subject = "Hourly Reminder"

        # HTML content with a clickable link (if needed)
        html_content = f"""
        <html>
          <body>
            <p>{message}</p>
          </body>
        </html>
        """

        # Plain text content as a fallback
        plain_text_content = message

        # Create a Mail object with both plain text and HTML content
        mail = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            plain_text_content=plain_text_content,
            html_content=html_content
        )

        try:
            # Send the email
            response = sg.send(mail)
            logging.info(f"Email sent to {email}! Status Code: {response.status_code}")
        except Exception as e:
            logging.error(f"An error occurred while sending email to {email}: {e}")

if __name__ == "__main__":
    send_email()
