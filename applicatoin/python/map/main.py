from email.message import EmailMessage
import ssl
import smtplib

message = input("who wold you like to send to? ")

email = 'abdullah.khafagy2@gmail.com'
password = 'sltiihdhtbhizlyn'


email_resiver = message

subject = "hello from the python file"

body ="""
the code is working
"""


em = EmailMessage()

em['From'] = email
em['To'] = email_resiver
em['subject'] = subject
em.set_content(body)


context1 = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context1) as smtp:
    smtp.login(email, password)
    smtp.sendmail(email, email_resiver, em.as_string())

