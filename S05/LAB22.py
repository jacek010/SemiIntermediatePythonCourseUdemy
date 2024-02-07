import smtplib
from email.mime.multipart import MIMEMultipart

mail_from = "your_mail@gmail.com"
mail_to = "friend_mail@gmail.com"
mail_subject = "Testowy email wyslany skryptem"
mail_body = '''
Siema

Wysyłam do Ciebie mój padawanie email napisany skryptem

Pozdro
'''

message = f'''From: {mail_from}
Subject: {mail_subject}

{mail_body}
'''

user="your_mail@gmail.com"
password="enter app password here"

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.helo()
    server.login(user, password)
    server.sendmail(user, mail_to, message)
    server.close()
    print('mail sent successfully!')
except:
    print('mail not sent!')
