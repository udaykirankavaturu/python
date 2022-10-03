# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC1ad71486d3fc833a44fc77b2147e2693'
auth_token = '535442ef79409033ca953f2366a919f4'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                    from_='+13029243491',
                    to='+919989308463'
                )

print(message.sid)
