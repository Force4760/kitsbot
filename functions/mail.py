#import modules
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secret.passw import sender, receiver, pw


def send(html, day):
    sender_email = sender
    receiver_email = receiver
    # sender email password
    password = pw

    message = MIMEMultipart("alternative")
    message["Subject"] = "New Kits " + day
    message["From"] = sender_email
    message["To"] = receiver_email

    # Add to parts
    part1 = MIMEText("New Kits", "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )