import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.zone.eu'
port = 465
login = 'YOUR EMAIL'
password = 'YOUR PASSWORD'

message = MIMEMultipart()
message['Subject'] = 'Test mail sent with Python'
message['From'] = 'YOUR EMAIL'
message['To'] = 'YOUR EMAIL'

text = 'Hi, this message was sent with Python script.'
html = '<h1>Hi, this message was sent with Python script.</h1>'

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(login, password)
    server.sendmail(login,  'YOUR EMAIL', message.as_string())