# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Get these credentials from http://twilio.com/user/account
account_sid = "AC4f13c39e2e5b0cf1fd1017be8fd944a7"
auth_token = "423fb88dee17931cdb345671ed665069"
client = TwilioRestClient(account_sid, auth_token)
 
# Make the call
call = client.calls.create(to="+19178265606",  # Any phone number
                           from_="+19173380736", # Must be a valid Twilio number
                           url="http://twimlets.com/message?Message%5B0%5D=Are%20you%20from%20Columbia%3F%20If%20yes%20press%201&Message%5B1%5D=Awesome!!%20%20%20")
print call.sid