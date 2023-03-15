"""
9. Python Standard Library, 15. Templates

Use HTML for template emails.
Create a HTML file.
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())


message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "letc18807@gmail.com"
message["subject"] = "This is a test"
body = template.substitute({"name": "John"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("python.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Insert username and password.
    smtp.login(" ", " ")
    smtp.send_message(message)
    print("Sent..")
