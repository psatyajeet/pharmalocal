# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC4f13c39e2e5b0cf1fd1017be8fd944a7"
auth_token = "423fb88dee17931cdb345671ed665069"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(to="+16099370216", from_="+19173380736",
                                     body="Take it easy boys!")