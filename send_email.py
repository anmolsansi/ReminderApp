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
    recipients = "test"
    if not SENDGRID_API_KEY:
        logging.error("SendGrid API key not set in environment variables.")
        return

    # Retrieve and decode the recipients data
    try:
        encoded_data = json.loads(os.environ.get('RECIPIENTS'))
        print(" not fuck")
    except:
        print("f")
        print("1"+os.environ.get('RECIPIENTS', "Fuck"))
        return

    # try:
#         recipients = json.loads(encoded_data)
#     except:
#         print("different")
#         encoded_data = {
# "anmolsansi@gmail.com": "https://www.linkedin.com/jobs/search/?currentJobId=4044475925&f_E=2%2C3&f_TPR=r86400&geoId=103644278&keywords=%22Software%20Engineer%22&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD",
# "anmolsansi08@gmail.com": "https://www.linkedin.com/jobs/search/?currentJobId=4044475925&f_E=2%2C3&f_TPR=r86400&geoId=103644278&keywords=%22Software%20Engineer%22&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD",
# }
#         try:
#             recipients = json.loads(encoded_data)
#         except Exception as e:
#             print(e)
        
    print(111111)
    return
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

    print(recipients)
    
    # Send emails to each recipient
    for email, message in encoded_data.items():
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
