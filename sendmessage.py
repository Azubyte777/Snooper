import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


smtp_port = 587                 # Standard Secure SMTP Port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

email_from = "testdev675@gmail.com"

pswd = 'myiywzqsbuvkodtd'


subject = 'Package Delivery'


def send_emails(email_list, message):
 
  for person in email_list:
   
    body = "Hello! Link here: " + message
   
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = person
    msg['Subject'] = subject
   
    msg.attach(MIMEText(body, 'plain'))
     
    text = msg.as_string()
   
    print("Connecting to the server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email_from, pswd)
    print("Successfully connected to the server")
    print()
   
    # Send emails to  "person" as list is iterated
    print(f"Sending email to: {person}...")
    TIE_server.sendmail(email_from, person, text)
    print(f"Email sent to: {person}")
    print()
   
  TIE_server.quit()
