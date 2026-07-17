#input formatting-->input()
#string input for 1 input
'''name=input()
print(name)
name=input("enter the username:")
print(name)
print(type(name))'''

#integer input-->int()-->age,values,quantity
'''age=int(input("enter the age:"))
print(age)
print(type(age))'''
#float input-->float()-->prices,temp,discounts
'''price=float(input("enter the price:"))
print(price)
print(type(price))'''

#costprice,sellingprice-->loss/profit 
'''cost_price=float(input("enter the cost price:"))
selling_price=float(input("enter the selling price:"))
loss=cost_price-selling_price
print("loss:" ,loss)'''

#multiple string inputs..
'''name,place=input("enter the details:").split()
print(name)
print(place)
name,place=input("enter the details:").split(',')
print(name)
print(place)'''

#multiple integer values-->map(int,input().split())
'''a,b=map(int,input("enter the values:").split(','))
print(a)
print(b)'''

#multiple float values-->map(float,input().split())
'''price,temp=map(float,input("enter the values:").split(','))
print(price)
print(temp)'''

#List of strings-->input().split()-->the values will be stored in the form of list in output
'''data=input("enter the details:").split(',')
print(data)'''

#list of integers-->list(map(int,input().split()))-->the values will be stored in the form of list in output 
'''marks=list(map(int,input("enter the marks:").split(',')))
print(marks)'''

#list of float values-->list(map(float,input().split()))-->the values will be stored in the form of list in output 
'''price=list(map(float,input("enter the marks:").split(',')))
print(price)'''

#ouput formatting
#print
'''print(25)
print(15,2.5,'codegnan')'''

#separator-->for separating the values
#print(2026,7,9)
#above case we want as date format
'''print(2026,7,9,sep='-')
print(2026,7,9,sep='/')
print('codegnan','AAA',sep='<------------->')'''

#end argument in print()-->\n-->new line
'''name='codegnan'
place='hyd'
course='AAA'
print(name,place)
print(course)
print(name,place,end=' ')
print(course)
print(name,place,end='\t')#\t-->tab space
print(course)'''

#checking in how many ways we can write the print()
#using commas
'''name='codegnan'
place='hyd'
print(name,place)
print("name:",name,"place:",place)
print("name:",name,"place:",place,sep=',')'''

#old style formatting-->%d,%s,%f
'''age=32
place='hyd'
print("age is %d and place is %s"%(age,place))
price=45.63
print("item price is %f"%(price))
print("item price is %.f"%(price))
print("item price is %.1f"%(price))
print("item price is %.2f"%(price))'''

#using str().format() method
'''name,course='lakshmi','python'
print("{} is enrolled in {} course".format(name,course))'''

#f-string notation--->Most recommended 
name,course='lakshmi','python'
print(f"{name} is enrolled in {course}")
























