card=True
pin=int(input("enter the pin:"))
'''total_amount=int(input("enter the  total amount:"))
savings=int(input("enter the savings amount:"))
withdrawl_amount=int(input("enter the withdrawl amount:"))
deposit=int(input("enter the deposit amount:"))'''
choice = input("Enter your choice (withdrawal/deposit/check balance/transactions): ")

pin_count=1
while pin!=2345:
    print(f"incorrect pin entered")
    if pin_count>=3:
        print(f"you can try to login after 24hrs")
        break
    pin_count+=1
    pin=int(input("enter the pin correctly:"))
    if choice==1
else:
    print("give the details correctly")
