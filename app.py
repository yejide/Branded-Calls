from twilio.rest import Client
import config


client = Client(config.account_sid, config.auth_token)

call = client.calls.create(
    url="https://handler.twilio.com/twiml/EHa0c9ab5d24fb36ad17906c582ac79693",
    to=config.my_number,
    from_="config.twillio_number"
)
print(call.sid)
