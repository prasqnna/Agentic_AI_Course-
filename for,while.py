'''price=int(input("enter the price:"))
if price>1000:
    print("Best Seller")
elif price<0:
    print("should not give negative price")
else:
    print("No Output")'''
#nested conditions---->one condition inside another---->if,else
'''syntax:
if condition:
    if condition2:
        statements(s).....
        .........
        elif condition3:
    else:
    statements......
'''
#usecase of : ATM withdrawl scenario:
'''correct_card=True
correct_pin=int(input("enter the pin"))
total_amount=int(input("enter the amount:"))
savings=int(input("enter the savings amount"))
withdrwal_amount=int(input("enetr the withdrwal amount"))
if correct_card==True and correct_pin == 4567:
    if current_amount>=savings:
         whithdrwal_amount=total_amount-savings
         print(withdrwal_amount)
    else:
        print("withdrwal is not possible")
else:
    print("invalid card or invalid pin")

#another way:
card_inserted=True
correct_pin=True
balance=10000
with_drawl_amount=int(input("enter the amount to withdrawl:"))
if card_inserted:
    if correct_pin:
        if balance>with_drawl_amount:
            print(f'transaction is successful,new balance is {balance-with_drawl_amount}')
        else:
            print(f'transaction failed, please maintain sufficient balance')
    else:
        print(f'wrong pin enterd')
else:
    print(f'your card is not valid')'''
#weekend planner based on budget
'''Budget=int(input("enter the price:"))
if Budget>10000:
    print("plan:",'Trip')
elif Budget>5000:
    print("plan:",'Resort Stay')
elif Budget>3000:
    print("plan:",'Movie and Dinner')
elif Budget>1000:
    print("plan:",'Cafe and Shopping')
elif Budget>500:
    print("plan:",'Street Food and Park Visit')
else:
    print("plan:",'Stay Home')

#another method
Budget=int(input("enter the price:"))
if Budget>0:
    if Budget>10000:
        print("plan:",'Trip')
    elif Budget>5000:
        print("plan:",'Resort Stay')
    elif Budget>3000:
        print("plan:",'Movie and Dinner')
    elif Budget>1000:
        print("plan:",'Cafe and Shopping')
    elif Budget>500:
        print("plan:",'Street Food and Park Visit')
    else:
        print("plan:",'Stay Home')
else:
    print("invalid Budget")'''








password=input("enter the password:")
password_count=1
while password!='admin':
    print(f'incorrect password')
    if password_count>=3:
        print("account freezed")
        break
    password_count+=1
    password=input(" enter the correct password")
else:
    print("login successful")





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
    '''if total_amount>savings:
        withdrawl_amount=total_amount-savings
        balance=total_amount-withdrawl_amount
        print("login successful")
        print(f'{withdrawl_amount} withdrawl_amount is possible')
        print(f'Balance amount is {balance}')
    elif pin_count>=3:
        print(f"you can try to login after 24hrs")
        break
    pin_count+=1
    pin=int(input("enter the pin correctly:"))'''
if pin==2345 and total_amount>savings:
        withdrawl_amount=total_amount-savings
        balance=total_amount-withdrawl_amount
        print("login successful")
        print(f'{withdrawl_amount} withdrawl_amount is possible')
        print(f'Balance amount is {balance}')
else:
    print("give the details correctly")
    
    





























    






















































    

















   
