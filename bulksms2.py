import africastalking

#initialize the sdk
username = "#"
api_key = "#"
africastalking.initialize(username,api_key)

#recipients
recipients = ['+254712345678']

#message
message = input("Enter your message: ")

#initialize the service, in our case, SMS
sms = africastalking.SMS

#USE THE SERVICE
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

#sms.send("Bulk SMS sending, testing phase 2. From PaulWababu", recipients, callback=on_finish)
sms.send(message, recipients, callback=on_finish)
