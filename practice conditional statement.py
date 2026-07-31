#conditional statements
#grade checker
marks=int(input("enter marks:"))
if marks>=90 and marks<=100:
    print('Grade:', 'A','\n','remark:','Outstanding!')
elif marks>=80 and marks<89:
    print('Grade:','B','\n','remark:','Excellent!')
elif marks>=70 and marks<79:
    print('Grade:','C','\n','remark:','Good')
elif marks>=60 and marks<69:
    print('Grade:','D','\n','remark:','Fair, needs improvement')
elif marks>=50 and marks<59:
    print('Grade:','E','\n','remark:','poor, needs improvement')
elif marks>=0 and marks<50:
    print('Grade:','F','\n','remark:','Failed,needs to reappear')
else:
    print('Invalid marks entered')

#even-odd
num=int(input("enter number:"))
if num==0:
    print("Zero is neither even or odd")
elif num<0:
    if num%2==0:
        print("negative even number")
    else:
        print("negative odd number")
elif num>0:
    if num%2==0:
        print("positive even number")
    else:
        print("positive odd number")

#season identifier
month=int(input("enter month number:"))
a=[[12,1,2],[3,4,5],[6,7,8],[9,10,11]]
if month in a[0]:
    print("winter")
elif month in a[1]:
    print("spring")
elif month in a[2]:
    print("summer")
elif month in a[3]:
    print("autumn")
else:
    print("invaild month entered")












        
