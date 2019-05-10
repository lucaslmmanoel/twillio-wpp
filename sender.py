# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


account_sid = 'your-token-here'
auth_token = 'your-token-here'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         from_='whatsapp:+14155238886',
         body='Oi Lucas tudo bem contigo?',
         to='whatsapp:+556183394739'
     )

print(message.sid)