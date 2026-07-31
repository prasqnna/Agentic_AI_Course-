#printing the values in dict
'''details={}
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


#handling zero division:
while True:
    try:
        weight=int(input("enter the weight:"))
        height=float(input("enter the hegiht:"))
        if weight>0 and height>0:
            print("valid input received")
            break
    except ValueError:
        print("make sure to enter only positive vales")
    except ZeroDivisionError:
        print("both zeroes are not allowed")
        continue
bmi=(weight)/((height)**2)
print(bmi)
if bmi<18.5:
    print(f"you are under weight as BMI is {bmi}")
elif bmi>=18.5 and bmi<=24.9:
        print(f"normal weight as BMI is {bmi}") 
elif 25<=bmi<=29.9:
        print(f"over weight as BMI is {bmi}")
elif bmi>=30:
    print(f"obesity as BMI is {bmi}")


#ATM
card=True
pin=int(input("enter the pin:"))
total_amount=int(input("enter the  total amount:"))
savings=int(input("enter the savings amount:"))
withdrawl_amount=int(input("enter the withdrawl amount:"))
pin_count=1
while pin!=2345:
    print(f"incorrect pin entered")
    if pin_count>=3:
        print(f"you can try to login after 24hrs")
        break
    pin_count+=1
    pin=int(input("enter the pin correctly:"))
if total_amount>savings:
        withdrawl_amount=total_amount-savings
        balance=total_amount-withdrawl_amount
        print("login successful")
        print(f'{withdrawl_amount} withdrawl_amount is possible')
        print(f'Balance amount is {balance}')
else:
    print("give the details correctly")
deposit=int(input("enter the amount:"))
if deposit:
    upadted_balance=balance+deposit
    print("upadated balance:",upadted_balance)
transcations=[]
transcations.append(withdrawl_amount)
transcations.append(deposit)
print(transcations)


def bmi(name,weight,height,unit):
    if unit=="m":
        height=height
    elif unit=="cm":
        height=height/100
    elif unit=="ft":
        height=height*0.3048
    bmi = (weight)/((height)**2)
    print(bmi)
    if bmi<18.5:
        print(f"you are under weight as BMI is {bmi}")
    elif bmi>=18.5 and bmi<=24.9:
        print(f"normal weight as BMI is {bmi}") 
    elif 25<=bmi<=29.9:
        print(f"over weight as BMI is {bmi}")
    elif bmi>=30:
        print(f"obesity as BMI is {bmi}")
#n = int(input("enter the number of executions:"))
name = input("enter the user name:")
weight =int(input("enter the weight in kgs:"))
height =float(input("enter the height:"))
unit=input("enter the unit (m/cm/ft)")
bmi(name,weight,height,unit)

def bmi_cal(*a):
    while True:
        try:
            weight=int(input("enter the weight:"))
            height=float(input("enter the hegiht:"))
            if weight>0 and height>0:
                print("valid input received")
                break
        except ValueError:
            print("make sure to enter only positive vales")
        except ZeroDivisionError:
            print("both zeroes are not allowed")
            continue

    
    
    bmi=(weight)/((height)**2)
    print(bmi)
    if bmi<18.5:
        print(f"you are under weight as BMI is {bmi}")
    elif bmi>=18.5 and bmi<=24.9:
            print(f"normal weight as BMI is {bmi}") 
    elif 25<=bmi<=29.9:
            print(f"over weight as BMI is {bmi}")
    elif bmi>=30:
        print(f"obesity as BMI is {bmi}")
bmi_cal()




#BMI using functions

def bmi(*args):
    bmi = (weight)/((height)**2)
    if bmi<18.5:
        print(f"{name}you are under weight as BMI is {bmi}")
    elif bmi>=18.5 and bmi<=24.9:
        print(f"{name} normal weight as BMI is {bmi}") 
    elif 25<=bmi<=29.9:
        print(f"{name} over weight as BMI is {bmi}")
    elif bmi>=30:
        print(f"{name} obesity as BMI is {bmi}")
n = int(input("enter the number of executions:"))
for i in range(n):
    name = input("enter the user name:")
    weight =int(input("enter the weight in kgs:"))
    height =float(input("enter the height:"))
    unit=input("enter the unit (m/cm/ft)")
    if unit=="m":
        height=height
    elif unit=="cm":
        height=height/100
    elif unit=="ft":
        height=height*0.3048
    bmi()




    


def bmi(**args):
    name=args["name"]
    weight=args["weight"]
    height=args["height"]
    
    
   
    for i,j in bmi.items:
        print(i,j)
        bmi = (weight)/((height)**2)
        
    
        if bmi<18.5:
            print(f"{name}you are under weight as BMI is {bmi}")
        elif bmi>=18.5 and bmi<=24.9:
            print(f"{name} normal weight as BMI is {bmi}") 
        elif 25<=bmi<=29.9:
            print(f"{name} over weight as BMI is {bmi}")
        elif bmi>=30:
            print(f"{name} obesity as BMI is {bmi}")
n = int(input("enter the number of executions:"))
for i in range(n):
    name = input("enter the user name:")
    weight =int(input("enter the weight in kgs:"))
    height =float(input("enter the height:"))
    unit=input("enter the unit (m/cm/ft)")
    if unit=="m":
        height=height
    elif unit=="cm":
        height=height/100
    elif unit=="ft":
        height=height*0.3048
    bmi(name=name,weight=weight,height=height)
'''

def atm(*args):
    if total_amount>savings:
            withdrawl_amount=total_amount-savings
            balance=total_amount-withdrawl_amount
            print("login successful")
            print(f'{withdrawl_amount} withdrawl_amount is possible')
            print(f'Balance amount is {balance}')
    else:
        print("give the details correctly")

    if deposit:
        upadted_balance=balance+deposit
        print("upadated balance:",upadted_balance)
    transcations=[]
    transcations.append(withdrawl_amount)
    transcations.append(deposit)
    print(transcations)
card=True
pin=int(input("enter the pin:"))
total_amount=int(input("enter the  total amount:"))
savings=int(input("enter the savings amount:"))
withdrawl_amount=int(input("enter the withdrawl amount:"))
deposit=int(input("enter the amount:"))
pin_count=1
while pin!=2345:
    print(f"incorrect pin entered")
    if pin_count>=3:
        print(f"you can try to login after 24hrs")
        break
    pin_count+=1
    pin=int(input("enter the pin correctly:"))
atm()

        
          
