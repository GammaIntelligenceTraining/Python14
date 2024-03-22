import smtplib, ssl

smtp_server = 'smtp.zone.eu'
port = 587
sender_email = 'python-learning@mrartful.com'
password_input = input('Enter password: ')

# Create secure ssl context
context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    '''
    To identify yourself to the server, .helo() (SMTP) or .ehlo() (ESMTP)
    should be called after creating an .SMTP() object, and again after .starttls().
    This function is implicitly called by .starttls() and .sendmail() if needed,
    so unless you want to check the SMTP service extensions of the server,
    it is not necessary to use .helo() or .ehlo() explicitly.
    '''
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password_input)
except Exception as e:
    print(e)
finally:
    print('Bye')
    quit()