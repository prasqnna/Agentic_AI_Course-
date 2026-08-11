'''
#pass by value 
#pass by object reference
'''
#pass by value refernce----->immutable objects(int,float,str,tuple,frozenset)
'''def update(number):
    """pass by value refernce works"""
    number=15
    number=number*5
    return number
print(update(5))
number=23
print(update(number))
print(number)
print(update("3"))


def update(s):
    """pass by value refernce works"""
    s="course"
    s=s+"AAI"
    return s
print(update(5))
s="python"
print(update(s))
print(s)
print(update("3"))

def update(number):
    return number*3
print(update(3))
print(update(25))
number=45
print(update(number))

#pass by object refernce--->mutable ojects(list,set,dict)
def my_list(a):
    a.append(5)
    a.insert(2,"codegnan")
    a.pop()
    return a
b= [1,2,3,4]
print(my_list(b))

#functions are termed as first class objects---->a function inside another function --->enclosing scope(non local)
#a function can be used as an argument to another function--->list(map(int,input()))
#a function can call itself(recursive functions)
#a function can return another function 



#bulit-in functions--->python by default has bulit-ins which makes the logic easier 
#print(dir(__builtins__))#list of all built ins(errors and functions)
#print(len(dir(__builtins__)))

#we will 
print(abs(-23))#returns the absolute value(+ve)
#all(),any()--->checks for the values in a iterable
data=["saketh","sai","akash"]
print(all(data))
data.clear()
print(all(data))
d=[None,23,45]
print(all(d))
print(any(d))
print(bin(6))#it returns binary represtation 
print(chr(65))#input any integer--->returns specific charater
print(bool(0))
print(complex())#returns complex number
print(dict(name="saketh",place="codegnan"))#returns a dictionary
print(divmod(3,5))#returns the division 
details=["codegnan","saketh","AAI"]
for i in details:
    print(details.index(i),':',i)

a=eval(input("enter the dict:"))
print(a)
b=(23,1,4,6)
print(sorted(b))#sorted by defult returns list
print(min(b))
print(max(['C','code','Data']))
print(pow(2,3))
print(tuple(reversed(b)))
print(round(4.5))
print(round(4.567,2))

details=["codegnan","AAI"]
ages=[7,1]
d=dict(zip(details,ages))#zip--->combines multiple coolections into one iterable(list,dict)
print(d)

#recursive functions, anonymous function 
#recursive function---->a function calling itself, where it makes the smaller problem is broken into multiple times
#depends on two cases---->base case(it indicates when to stop the base condition)
#another case---->recuesive case(it makes the problem to be repeated)
syntax:
def function():
    if base_condition:
        return
    function()#we write our recursive
function()

def test():
    """without base case"""
    return test()
print(test())


#factorial using recursion
def factorial(n):
    if n>=0:
        if n==0 or n==1:
            return 1
        else:
            return n*factorial(n-1)
    elif n<0:
        return ("give only positive values")
n=int(input("enter the value: "))
print(factorial(n))

#sum of 10 numbers
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
n=int(input("enter the num:"))
print(sum(n))

#task: build sample choice chooser
#1-->recursion logicc for factorial
#2--->sum of numbers
#3--->BMI calculate
#5--->Fibonacci series
#5---->ATM usecase

#Anonymous functions--->name less functions , we define them by using lambda keyword
#filter(),map()
#create a function to return the area of rectangle
def rectangle(l,b):
    area=l*b
    return area
l=float(input("enter the length:"))
b=float(input("enter the b:"))
print(rectangle(l,b))

#syntax:--->var_name=lambda parameters: expression
b=lambda l,b: l*b
print(type(b))
print(b(6,5))

a=lambda s: s**2
print(a(4))

#user registration in a webpage--->name
d=lambda first_name,last_name:first_name+" " + last_name
first_name=input().title()
last_name=input().title()
print(d(first_name,last_name))


first_name=input()
last_name=input()
def full_name(first_name,last_name):
    return first_name.title()+ " "+last_name.title()
print(full_name(first_name,last_name))


#even number:
n=int(input("enter the value:"))
result=lambda n: "Even" if n%2==0 else "Odd"
print(result(n))

#length of sequences
name=input("enter the message:")
result=lambda name:len(name)
print(result(name))

#filter(),map()
#filter(function,iterable)---->returns the filtered values by satisfying the conditions yielding the value from iterable
a=list(map(int,input("enter the values:").split(",")))
print(a)
#filter only even numbers
b=list(filter(lambda x:x%2==0,a))
print(b)

a=['pavan','abhiram','nihanth','saikiran','vasanthi','manimala']
b=list(filter(lambda x:len(x)>6,a))
print(b)

#map()---->it will apply for every value in an iterable
a=list(map(int,input("enter the values:").split(",")))
print(a)

names=['codegnan','saketh','agenticai']
result=list(map(lambda name:name.upper(),names))
print(result)

prices=[1000,2500,3500,4000]
final_price=list(map(lambda price:price-(price*0.1),prices))
print(final_price)
'''
#reduce()-->this makes complete iterable to be a single value--->functools
from functools import reduce
numbers=[1,4,5,7,8]
result=reduce(lambda a,b:a+b,numbers)
print(result)
product=reduce(lambda a,b:a*b,numbers)
print(product)







