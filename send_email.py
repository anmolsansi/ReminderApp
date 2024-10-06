import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To
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

    # Website link to include in the email
    website_url = os.environ.get('Link')  # Replace with your website link

    # HTML content with a clickable link
    html_content = f"""
    <html>
      <body>
        <p>This is your hourly reminder to stay focused and productive!</p>
        <p>Click <a href="{website_url}">here</a> to visit the website.</p>
      </body>
    </html>
    """

    # Plain text content as a fallback
    plain_text_content = f"This is your hourly reminder to stay focused and productive! Visit the website at: {website_url}"

    # Create a Mail object with both plain text and HTML content
    mail = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        plain_text_content=plain_text_content,
        html_content=html_content
    )

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
