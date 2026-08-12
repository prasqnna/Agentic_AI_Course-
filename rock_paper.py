while True:
    print("1. Rock Paper Scissors")
    print("2. Story Generator")
    print("3. BMI Calculator")
    print("4. OTP Email")
    print("5. Exit")

    ch = int(input("Enter your choice: "))
    if ch==1:
        import random
        player1=input("enter the choice:--->rock,paper,scissors")
        player2=random.choice(['rock','paper','scissors'])
        print("playesr2 selection:",player2)
        if player1=='rock' and player2=='paper':
            print("player2 wins")
        elif player1=='rock' and player2=='scissors':
            print("player1 wins")
        elif player1=='paper' and player2=='rock':
            print("player1 wins")
        elif player1=='paper' and player2=='scissors':
            print("player2 wins")
        elif player1=='scissors' and player2=='rock':
            print("player2 wins")
        elif player1=='scissors' and player2=='paper':
            print("player1 wins")
        else:
            print("tie")
    elif ch==2:
        import random

        when = [
            "Yesterday",
            "Last week",
            "One morning",
            "At midnight",
            "On Sunday"
        ]

        who = [
            "a little girl",
            "a brave soldier",
            "an old man",
            "a curious student",
            "a clever dog"
        ]

        where = [
            "in the forest",
            "at the beach",
            "inside a castle",
            "in the park",
            "near the river"
        ]

        what = [
            "found a hidden treasure.",
            "met a magical fairy.",
            "rescued a lost child.",
            "discovered a secret cave.",
            "won a big competition."
        ]

        story = (
            random.choice(when) + ", " +
            random.choice(who) + " " +
            random.choice(what) + " " +
            random.choice(where)
        )

        print("Generated Story:")
        print(story)
    elif ch==3:
        details={}
        n = int(input("enter the number of executions:"))
        for i in range(n):
            name = input("enter the user name:")
            #weight = 70
            weight =int(input("enter the weight in kgs:"))
            #height = 1.65
            height =float(input("enter the height:"))
            unit=input("enter the unit (m/cm/ft)")
            if unit=="m":
                height=height
            elif unit=="cm":
                height=height/100
            elif unit=="ft":
                height=height*0.3048
            bmi = (weight)/((height)**2)
            if bmi<18.5:
                    body_type="you are under weight"
            elif bmi>=18.5 and bmi<=24.9:
                body_type="normal weight" 
            elif 25<=bmi<=29.9:
                body_type="over weight"
            elif bmi>=30:
                body_type="obesity "
            details[name]={"BMI":round(bmi,2),
                           "BODY_TYPE":body_type}
            print(details)
    elif ch==4:
        import smtplib
        import email
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        import random
        import json
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
        text=msg.as_string()
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
    elif ch==5:
        print("thank you")
        break
    else:
        print("invalid ")

#ticket booking

import random
from datetime import date
print("welcome to moviemate AI!")
name=input("enter your name:")
print("\n1.Action","\n2.Comedy","\n3.Horror","\n4.Romance")
action = ["Leo", "Vikram", "Jailer"]
comedy = ["Leo", "Vikram", "Jailer","Jathi Ratnalu", "F2", "DJ Tillu"]
horror = ["Leo", "Vikram", "Jailer","Arundhati"]
romance = ["Sita Ramam", "Hi Nanna"]
while True:
    choice=int(input("enter the number:"))
    if choice==1:
        print(action)
    elif choice==2:
        print(comedy)
    elif choice==3:
        print(horror)
    elif choice==4:
        print(romance)
    elif choice==5:
        print("thankyou")
    else:
        print("invalid")
    movie=input("enter the movie:")
    times = ["10:00 AM","1:30 PM","4:30 PM","7:30 PM","10:15 PM"]
    show_time = random.choice(times)
    booking_date = date.today()
    print("\nBooking Confirmed!")
    print("Customer    :", name)
    print("Movie       :", movie)
    print("Show Time   :", show_time)
    print("Booking Date:", booking_date.strftime("%d-%b-%Y"))
    print("\nEnjoy your movie!")
    break
    
    
        

    






















