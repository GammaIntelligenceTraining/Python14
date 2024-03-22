import smtplib, ssl

# testerpython@mrartful.com
# 123helloWORLD

port = 465
password_input = input('Enter password: ')

# Create secure ssl context
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.zone.eu', port, context=context) as server:
    server.login('python-learning@mrartful.com', password_input)
