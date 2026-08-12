#armstrong number
'''n=int(input("enter the number:"))
digits = len(str(n))
total = 0
org=n
for i in range(digits):
    digit = n % 10
    total += digit ** digits
    n //= 10
if total==org:
    print("Armstrong Number")
else:
    print("Not Armstrong Number") 
  
#3 test scores
a=int(input("enter the scorce:"))
b=int(input("enter the scorce:"))
c=int(input("enter the scorce:"))
if a<b<c:
    print("improving")
elif a>b>c:
    print("Declinig")
else:
    print("invalid input")

#mobile usage
a=float(input("enter the usage:"))
b=input("enter unit:")
if a<1:
    print("Plan A")
elif a>=5:
    print("plan B")
elif a<5:
    print("Plan C")

#Bmi
height=float(input("enter the height:"))
weight=int(input("enter the weight:"))
bmi=weight/height**2
if bmi<18.5:
    print("under weight")
elif 18.5<bmi<24.9:
    print("normal weight")
elif 25.0<bmi<29.9:
    print("over weight")
else:
    print("obese")

#even numbers
n=int(input("enter the mnumber:"))
if n>0:
    for i in range(n,1,-1):
        if i%2==0:
            print(i)
else:
    print("invalid input")

#square pattern
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*i,end=" ")
    print("")

  
#divisible of 3
n=int(input("enter the number:"))
count=0
for i in range(1,n):
    if i %3==0:
        count+=1
print(count)
        

#mul
n=int(input("enter the number"))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')
'''
#removing ,
my_list=[54,43,2,1,5]
for i in my_list:
    print(i,end=" ")
print()




























