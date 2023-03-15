"""
11. Popular Python Packages, 06. Sending Text Messages

Twilio is a popular communication platform.
Can send text, video, and voice calls. 
Create a Twilio account for free. 
"""
from twilio.rest import Client
import config

account_sid = config.account_sid
auth_token = config.auth_token

client = Client(account_sid, auth_token)

client.messages.create(
    to="...",
    from_="...",
    body="This is our first message"
)
