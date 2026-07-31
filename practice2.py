#Airline dynamic pricing
'''base_price=5000
seat=input()
days=int(input("enter the days:"))
season=input("enter the season:").lower()=='true'
age=int(input("enter the age:"))
if seat=="business seat" :
    bill=base_price*1.40
elif seat=="premium economy" :
    bill=base_price*1.20
elif seat=="economy" :
    bill=base_price
if days<7:
    bill=bill*1.25
elif days>30:
    bill=bill*0.9
if season==season:
    bill=bill*1.20
if age>60:
    bill=bill*0.85
print(bill)

bill=10000
age=int(input("enter the age:"))
health_score=int(input("enter the value:"))
vehicle=input().lower()
if age<25:
    bill=bill*1.20
elif age>50:
    bill=bill*1.15
if health_score>=80:
    bill=bill*0.9
elif health_score<60:
    bill=bill*1.20
if vehicle=='sports car':
    bill=bill*1.30
elif vehicle=='suv':
    bill=bill*1.15
print(bill)

credit=int(input("enter the value:"))
income=int(input("enter the income:"))
liabilites=int(input("enter the value:"))
if credit>=750:
    credit='eligible'
elif credit>650 and credit<749:
    credit='conditional eligible'
elif credit<650:
    credit='not eligible'
if income>=50000:
    income='eligible'
if liabilites<=20000:
    liabilites="eligible"
if credit=="eligible" and income=="eligible" and liabilites=='eligible':
    print("approved")
elif credit=="conditional eligible" and income=="eligible" and liabilites=='eligible':
    print("approved with conditions")
else:
    print("rejected")
'''
salary=int(input("enter the salary:"))
rating=int(input("enter the rating:"))
exp=int(input("enter the exp:"))
att=int(input("enter the att:"))
bill=0
if rating==5:
    bill+=salary*0.25
elif rating==4:
    bill+=salary*0.15
elif rating==3:
    bill+=salary*0.10
elif rating<3:
    bill+=salary
if exp>=10:
    bill+=salary*0.10
elif exp>=5 and exp<10:
    bill+=salary*0.05
elif exp<5:
    bill+=salary
if att>=95:
    bill+=salary+5000
elif att>=85 and att<=94:
    bill+=salary+2000
elif att<85:
    bill+=salary
print(bill-salary)
                


    


    



    
       
    
