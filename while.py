'''
repetition statements------>for,while

while---->checks until and unless the given condition is satisfied(True)
syntax:
while condition:
    statements(s).....
    ........
'''

#simple usage
'''count=0
while count<5:
    print("okay you have access")
    a=[]
    a.append("codegnan")
    print(a)
    count=count+1#addition assignment operator'''
    
#checking the valid attempts
'''count=5
while count>=1:
    print(f'count={count}')
    count=count-1'''

#to find a valid passward:
'''password=input("enter the password:")
password_count=1
while password!='admin':
    print(f'incorrect password')
    if password_count>=3:
        print("account freezed")
        break
    password_count+=1
    password=input(" enter the correct password")
else:
    print("login successful")'''


#for with else,while with else----->else will be executed only when loop is completely done
#search for a product in the store
'''search=input("enter the search item:").lower()
store=['mobile','laptop','powerbank','chager']
for item in store:
    if search==item:
        print(f'item is found')
        break
else:
    print(f'item is not found')'''
#break,continue,pass--->jumping statements
#break---->it terminates the loop once the given condition is satisfied
#continue-->it basically skips the current iteration and gets back to the next itration

'''for i in 'codegnan':
    if i=='g':
        continue
    print(i)'''

'''for i in 'codegnan':
    if i=='g':
        break
    print(i)'''
#pass-->it is generally used as a placeholder (to have any syntax matches)
'''for i in range(10):
    pass
    #print("hello")'''

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
if pin==2345 and total_amount>savings:
        withdrawl_amount=total_amount-savings
        balance=total_amount-withdrawl_amount
        print("login successful")
        print(f'{withdrawl_amount} withdrawl_amount is possible')
        print(f'Balance amount is {balance}')
else:
    print("give the details correctly")
    
    
    
    















    
        
    

















    

