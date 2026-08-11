'''
we want to send automated email using python by adding attachemnt(file)

import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
#same include mailwith subject code
From="prasannabont@gmail.com"
To="manimalanama24@gmail.com"
Subject="Agentic AI Classes"
app_password='eqio nylz okth cmmt'
body='In this project we will understand how python can be useful in real world applications'
attach='Simpleemail.py'#give your attachment name
msg=MIMEMultipart()
msg["From"]=From
msg["To"]=To
msg["Subject"]=Subject
msg.attach(MIMEText(body))
#now we need to add file attachment
part=MIMEBase("application","octet-stream")
part.set_payload(open(attach,'rb').read())
encoders.encode_base64(part)
part.add_header("Content-Disposition",'attachment;filename="%s"'%(os.path.basename(attach)))
msg.attach(part)
text=msg.as_string(part)
#start the sever communication 
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(From,app_password)
server.sendmail(From,To,text)
print("mail sent")
server.quit()
'''


import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
#same include mailwith subject code
From="prasannabont@gmail.com"
bulk_email={"manimalanama24@gmail.com","lakshmiprasannabonthala@gmail.com","navyasriyallampalli3@gmail.com"}

Subject="Agentic AI Classes"
app_password='eqio nylz okth cmmt'
body='In this project we will understand how python can be useful in real world applications'
attach='Simpleemail.py'#give your attachment name
msg=MIMEMultipart()
for To in bulk_email:
    msg["From"]=From
    msg["To"]=To
    msg["Subject"]=Subject
    msg.attach(MIMEText(body))
    #now we need to add file attachment
    part=MIMEBase("application","octet-stream")
    part.set_payload(open(attach,'rb').read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition",'attachment;filename="%s"'%(os.path.basename(attach)))
    msg.attach(part)
    text=msg.as_string(PendingDeprecationWarning)
    #start the sever communication 
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(From,app_password)
    server.sendmail(From,To,text)
    print("mail sent")
server.quit()

