'''
in this usecase(mini project),we will make use of control block statements
#BMI---->body mass index --->bmi=(weight(kg)/(height**2)(metres)

n=int(input("enter the value of members:"))
for i in range(n):
    name=input("enter the name")
    weight=float(input("enter the weight: "))
    height=float(input("enter the height: "))
    #>18.5--->under weight,18.5-24.9-->normal weight,25-29.9-->over weight
    if weight>0 and height>0:
        bmi=(weight)/((height)**2)
        if bmi<18.5:
            print(f"{name} you are under weight as BMI is {bmi}")
        elif bmi>=18.5 and bmi<=24.9:
            print(f"{name} normal weight as BMI is {bmi}") 
        elif 25<=bmi<=29.9:
            print(f"{name} over weight as BMI is {bmi}")
        elif bmi>=30:
            print(f"{name} obesity as BMI is {bmi}")
    else:
        print("enter the positive values")

#task---for same above bmi calculator store the values in dictionary
o/p---->BMI_results={'name':[user1,user2,user3]
                      'bmi':[bmi1,bmi2,bmi3]}
user height should be converted into meters'''
#exception handling--->try,except,finally
'''
try:
    statements(s)....
    ........
except errorname:
    debuging..........
finally:
    result.....

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
    print(f"{name} you are under weight as BMI is {bmi}")
elif bmi>=18.5 and bmi<=24.9:
        print(f"{name} normal weight as BMI is {bmi}") 
elif 25<=bmi<=29.9:
        print(f"{name} over weight as BMI is {bmi}")
elif bmi>=30:
    print(f"{name} obesity as BMI is {bmi}")
'''
#task2 handle the zerodivisionerror
#task3 build an ATM Calculator---->user account,pin verfication,check balance,withdraw,deposit,transactions-->limit the valid pin 
    
