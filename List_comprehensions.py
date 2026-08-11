'''
List comprehensions--->in python its a precise/easiest way to create lists
syntax: [expression for item in iterable]
iterable-->list,tuple,set,dict or range()
'''
#we need to append elements into list
'''list=[]
for i in range(10):
    list.append(i)
    print(list)

#the same above using list comprehension 
list=[i for i in range(10)]
print(list)


#set squrae
data=[i*i for i in range(10)]
print(data)

e=[i%2==0 for i in range(10)]
print(e)

details=['saketh','codegnan','data','agents','rag']
new=[i.upper() for i in details]
print(new)
print(*new)


a,*name,b=1,'saketh','codegnan','data',34
print(a)
print(name)#in this case we get a list
print(*name)#in this case all of values will return side by side
print(b)

a=[15,20,25,35]
#update the list by 5
a=[i+5 for i in a]
print(a)

#get the first letter of each object
data=['codegnan','agets','rag']
letter=[i[0] for i in data]
print(letter)

#list comprehensions with list
#[expression for item in iterable/range if condition]
collection=list(map(int,input("enter the values").split(",")))
print(collection)
result=[i for i in collection if i%2==0]
print(result)
b=list(filter(lambda x:x%2==0,collection))
print(b)

collection=list(map(int,input("enter the values").split(",")))
print(collection)
final=[i for i in collection if i>10]
print(final)
#list comprehension with if-else condition
#[true_value if codition else false_value for item in iterable]
data=[12,3,4,6,7,9]
print(data)
result=["new" if i%2==0 else "old" for i in data]
print(result)

#nested comprehension
#nested--->one inside another
#[expression for i in iterable1 for j in iterable2]
a=[(i,j) for i in range(5) for j in range(3)]
print(a)
b=[(i,j) for i in [1,4,5] for j in [2,3]]
print(b)
c=[i*j for i in range(1,11) for j in range(1,11)]
print(c)
colors=['red','blue','green']
sizes=['S','M','L']
dress=[(i,j) for i in colors for j in sizes]
print(dress)
#nested comprehension with if condition
c=[i*j for i in range(1,11) for j in range(1,11) if i!=j]
print(c)
#nested comprehension with if else
#[true_value if condition else false_value for i in iterable1 for j in iterable2]
a=[1,3,5,6,7]
b=[2,4,6,8,9]
c=[i+5 if i<j else i for i in a for j in b]
print(c)
a=[1,3,5,6,7]
b=[2,4,6,8,9]
c=(i+5 if i<j else i for i in a for j in b)#no tuple comprehension
print(c)'''
#in the above case if we replace [] braces with () we dont get tuple ---->generator
#no tuple comperhension ---->generator
#generator---->generator is a special function which produces one value at a time
#we use yield keyword
#normal function
'''
def fname():
    """doc string"""
    return value(s)
fname()

def fname():
    """doc string"""
    yield value1
    yield value2
    yield value3
fname()

def fun():
    """normal function"""
    return [1,2,3,4]
print(fun())
a=fun()
for i in a:
    print(i)
def fun():
    """generator function"""
    yield 1
    yield 2
    yield 3
b=fun()
print(next(b))
print(next(b))
print(next(b))
print(next(b))#stopiteration
'''
def display():
    """subjects covered"""
    yield "python"
    yield "genai"
    yield "rag"
    yield "agents"
print(display())
print(type(display()))
d=display()
print(next(d))
