#now in this case we will use email package where we can add subject to the mail and also we can give to addresss
'''import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#give from address,to address and subject
From="prasannabont@gmail.com"
To="manimalanama24@gmail.com"
Subject="Agentic AI Classes"
msg=MIMEMultipart()
msg['From']=From
msg['To']=To
msg['Subject']=Subject
body="Today we have python class"
msg.attach(MIMEText(body,'PLAIN'))
#entrie message to string format
text=msg.as_string()
#same as previous SMTP usage we will follow
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login('prasannabont@gmail.com','eqio nylz okth cmmt')
server.sendmail(From,To,text)
print("mail sent")
server.quit()
'''
#send an otp to user and validate it
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import json
#give from address,to address and subject
From="prasannabont@gmail.com"
To="manimalanama24@gmail.com"
Subject="Agentic AI Classes"
msg=MIMEMultipart()
msg['From']=From
msg['To']=To
msg['Subject']=Subject
otp=random.randint(1000,9999)
body=f"The otp is {otp} "
msg.attach(MIMEText(body,'PLAIN'))
#entrie message to string format
text=msg.as_string()
#same as previous SMTP usage we will follow
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login('prasannabont@gmail.com','eqio nylz okth cmmt')
server.sendmail(From,To,text)
print("mail sent")
a=int(input("enter the otp:"))
if a==otp:
    print("Login successful")
else:
    print("Login failure")

