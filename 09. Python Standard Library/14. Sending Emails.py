"""
9. Python Standard Library, 14. Sending Emails

Send emails with a script.
Import the following modules.

If using Gmail, enable two factor authentication and app password. 
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "letc18807@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("python.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Insert username and password.
    smtp.login(" ", " ")
    smtp.send_message(message)
    print("Sent..")
