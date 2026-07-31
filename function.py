def factorial(n):
    if n>0:
        if n==0 or n==1:
            return 1
        else:
            return n*factorial(n-1)
    elif n<0:
        return "give only positive values"

def sum(num):
    if num==1:
        return 1
    else:
        return num+sum(num-1)

def fibonacci(a,b,n):
    if n==0:
        return a
    elif n==1:
        return b
    for i in range (2,n+1):
        c=a+b
        a=b
        b=c
    return c

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

def main():
    print("\n======menu========")
    print("1.factorical")
    print("2.sum of n numbers")
    print("3.fibonacci")
    print("4.BMI")
    print("5.ATM")
    choice=int(input("enter a choice:"))
    if choice==1:
        n=int(input("enter a value of n:"))
        print(factorial(n))
     
        
    elif choice==2:
        num=int(input("enter the num:"))
        print(sum(num))
      
    elif choice==3:
        n=int(input("enter the number:"))
        a=0
        b=1
        print(fibonacci(a,b,n))
       
    elif choice==4:
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
        print(bmi(n,name,weight,height,unit))
    elif choice==5:
        print("exit")
       
    else:
        print("invalid")

  

main()

   


