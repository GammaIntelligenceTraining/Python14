import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
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
message['Bcc'] = 'mr.artfulx@gmail.com'  # message copy

text = '''\
Hi, this message was sent by Python script for test purpouses.'''

message.attach(MIMEText(text, 'plain'))

with open('picture.png', 'rb') as attachment:
    image = MIMEImage(attachment.read())


image.add_header(
    'Content-Disposition',
    f'attachment; filename={attachment}'
)

message.attach(image)
text = message.as_string()

# Create secure ssl context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password_input)
    server.sendmail(sender_email, reciever_email, message.as_string())