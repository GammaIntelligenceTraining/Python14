import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.zone.eu'
port = 465
sender_email = 'python-learning@mrartful.com'
reciever_email = 'roman.kutselepa@gmail.com'
password_input = input('Enter password: ')

# NOTE message is now created through MIMEmultipart module
message = MIMEMultipart()
message['Subject'] = 'Test email with python script.'
message['From'] = sender_email
message['To'] = reciever_email

text = '''\
Hi, this message was sent by Python script for test purpouses.'''

html = '''\
<html>
    <body>
        <h2>This is a test email</h2>
        <p style="color: red;">If you see this, then you received an html mail not plain text!</p>
    </body>
</html>
'''

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Remember to add the HTML message after the plain-text alternative,
# as email clients will try to render the last subpart first.
message.attach(part1)
message.attach(part2)

# Create secure ssl context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password_input)
    server.sendmail(sender_email, reciever_email, message.as_string())