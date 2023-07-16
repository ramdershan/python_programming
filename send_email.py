from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = 'Ram Dershan'
message['to'] = 'someonesemail'
message['subject'] = 'subject'
message.attach(MIMEText("somemessage"))

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls() # tls mode 'transport layer security'
    smtp.login('myemail', 'password') #for google and maybe others need to make and use a 16-digit app password
    smtp.send_message(message)
    print("Sent...")


