'''
step1:---->setting up gmail app password
'''
import smtplib
#first we will make the portocol connection
server=smtplib.SMTP("smtp.gmail.com",587)
print(server)
#start commucation
server.starttls()
#we will make the login
server.login("prasannabont@gmail.com",'eqio nylz okth cmmt')
print("login sucessful")
message="welcome to my world..This is an Automated Mail"
#send the mail
server.sendmail('prasannabont@gmail.com','manimalanama24@gmail.com',message)
print("success")
