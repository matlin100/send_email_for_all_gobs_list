import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

load_dotenv()  # This loads the environment variables from a .env file located in the same directory as this script.

# Environment variables for sensitive information
GMAIL_USER = os.getenv('GMAIL_USER')
GMAIL_APP_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')

def send_emails(to_list, subject, text, file_path=None):
    successful_emails = []
    failed_emails = []

    for to in to_list:
        server = None
        try:
            # Set up the SMTP server
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)

            # Create a MIMEMultipart message
            msg = MIMEMultipart()
            msg['From'] = GMAIL_USER
            msg['To'] = to['emailAddress']
            msg['Subject'] = subject

            # Add text and HTML to the message
            msg.attach(MIMEText(text, 'plain'))
            msg.attach(MIMEText(f'<p style="font-size: 18px; color:blue">{text}</p>', 'html'))
            msg.attach(MIMEText(f'<a href="https://matlin100.github.io/Chezky-Matlin-Portfolio/" target="_blank">Visit my website</a>', 'html'))

            # Attach a file if path is provided
            if file_path:
                with open(file_path, 'rb') as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
                    msg.attach(MIMEText('<p style="font-size: 14px; color: gray">Attaching CV</p>', 'html'))
                    msg.attach(part)

            # Send the email
            server.send_message(msg)
            successful_emails.append(to)
            print(f'Email sent successfully to {to}!')
        except Exception as e:
            print(f'Error occurred while sending email to {to}: {e}')
            failed_emails.append(to)
        finally:
            if server:
                server.quit()

    return successful_emails, failed_emails


