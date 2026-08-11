
'''pop-->procedure oriented programming---->function
function---->a function is a block of code which performs a specific task
it is a resuable code--->readbility,reusability and easy to maintain
user defind functions--->def
bulit-in functions--->python by default
anonymous functions-->lambda(map,filter,reduce)
recursive functions--->factioral,fibonacci---->decorators

syntax--->user defind functions
def fname(parameters):
    """doc string(description of function)"""
    statements....
    return value(s).....
fname(arguments)#function call

#sample function:
def add(a,b):
    """sample add function"""
    c=a+b
    #print(f'value of c is {c}')
    return c
#add(12,3)
#add(23.5,3)
#add('code','gnan')
print(add('code','gnan'))
#assigning function to a varible
result=add([1,2,3],[4,5,6])
print(result)
#parameters--->below categoriers
#positional arguments--->count of arguments to be matched
#default arguments---->we can make argument as default
#keywords arguments---->order/keyword name to be matched
#variable arguments(*args)------>we can pass any number of positional arguments can be given
#keyword variable length arguments(**kwargs)---->we can pass any number of keyword arguments
def grocery(item,price):
#def grocery(item,price=40):
#def grocery(item='jam',price):#nondefault is always follows default
#def grocery(item='bread',price=40):
    """usage of positional,default and keyword arguments"""
    print(f'item is {item}')
    print(f'value of item is {price}')
#grocery('milk',30)
#grocery('bread')
#grocery()
grocery(price=45,item='milk')
grocery(price=45,Item='milk')#typeerror---->keyword item is mismatching

#variable length arguments---->we can define any number of positional arguments
#python stores in tuple format,we use *  notation to define variable length arguments
def sample(*args):
    """usage of variable length arguments"""
    print(args)
    print(type(args))
sample()
sample(1,2,3)
sample(1,23.5,'codegnan',23+5j)
#sample(name="saketh")#type error

def add(*a):
    result=0
    print(a)
    #while type(a)!=str and type(a)==float:
    for i in a:
        if type(i) in (int,float):
            print(i)
            result=result+i
    return result
print(add(1,4,'codegnan'))

#keyword variable length arguments---->any number of keyword arguments can be passed 
#data is stored in dictionary---->we use ** notation
def sample(**kwargs):
    print(kwargs)
    print(type(kwargs))
sample()
sample(name="abhi",age=20,course="AAI")
#sample(name="abhi",36,age=20,course="AAI")#syntax error 

def grocery(**items):
    for i in items:
        print(i)
    for i in items.values:
        print(i)
    for i,j in items.items():
        print(f"key is {key}")
        print(f"value is {value}")
grocery(name='milk',price=35,quantity='1000ml',brand='heritage')

#scope of variables---->scope---->the filed (place) where we are accessing the variables
#local variables
#gobal variables
#enclosing variables(nongobal keyword)
#local variables---->the variables defined inside the functions
def fname():
    name="codegnan"#local variable
    return name
print(fname())
#print(name)#name error

#gobal variable---->it is defined and accessiable in the entire module(entrie python script)
name='codegnan'
def uname():
    name="saketh"
    return name
print(uname)
print(f"company name is {name}")
print(name+'AAI')

count=15
def update():
    global count
    count=count+10
    return count
print(update())
print(f"updated value of count is {count}")'''
#enclosing scope---->non local keywods---->nested functions
def outer():
    count=10
    def inner():
        nonlocal count
        count=count+5
        return count
    print(inner())
    return count
print(outer())
#LEGB---->local scope,enclosing scope,global,bulit-in
#bulit-in scope ------>bulit-in functions can be used as variables but it overrides its behaviour
#(should be avoided)
len=34
print(len)
#print(len('codegnan'))#here its overrides
