#control statements ===>these are the statements which control flow of execution of the program
#conditional statements(if,elif,else)---->nested if satements
#repetition statements (LOOPS)--> for , while---->nested loops(patterns)
#jumping statements--->break,continue,pass,assert


#if statement :
'''if <condition>:
    statements(s)...
    ........
    .....
 '''
#validate the price....
'''money=100
if money<=100:
    print(f"now you are eligible to get your items")
money=int(input("enter the billing price:"))#dynamic input
if money<=100:
    print(f"now you are eligible to get your items")
print("check again")

students=['ram','akash','abhi','mani']
name=input("enter the name:").lower()
if name in students:
    marks=50
    grade='A'
    print(f'{name} has secured {marks} marks and {grade} grade')'''
#(if-else)
'''syntax:
if <condition>:
    statements(s)
    .........
else:
    statement(s)
    


#vote eligibility
age=int(input("enter the age: "))
if age>=18:
    print("vote is eligible")
    print("your age is {} years, eligible".format(age))
else:
    #age=18-age
    #print(f"after {age} years you can vote")
    print(f'you need to wait for {18-age} years to get vote right')'''

#if-elif-else statements(s)
#for same above vote 
age=int(input("enter the age: "))
if age>=18:
    print("vote is eligible")
    print("your age is {} years, eligible".format(age))
elif age==0 or age<0:
    print(f'enter only positive values')
else:
    #age=18-age
    #print(f"after {age} years you can vote")
    print(f'you need to wait for {18-age} years to get vote right')










    






