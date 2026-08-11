'''
module--->user difine module ---->creating,accessing
bulit-in modules--->os,sys,random,math,platform,collections,itertools.....
A module is a python file(.py),we use import keyword
'''
'''import my_module
print(dir(my_module))#use dir to get available methods and attributes
print(my_module.greet("saketh"))
print(my_module.names)
print(type(my_module.names))
my_module.names.update({'place':'hyd','age':7})
print(my_module.names)
print(type(my_module.display()))'''

#accessing methods/attributes using from keyword
'''from my_module import greet
print(greet("agents"))
#print(names) #nameerror as we did not import 
from my_module import greet,names
print(greet("agents"))
print(names)
#print(display)#again we get a name error

#to access all methods/attributes we use *
#recommended only for userdefined/simple modules
from my_module import*
print(greet("saketh"))
names.update({"course":"AAI"})
print(names)
y=display()
print(next(y))
print(__name__)
print(__doc__)
print(my_module.__doc__)
print(my_module.__name__)'''

#built-in module--->math,os,sys,random,json,collections,itertools
#math--->it has all mathematial constants,trigonometric functions and basic math functions

'''import math
#print(dir(math))
print(math.__doc__)#it gives description about the module
print(math.ceil(2.5)) #it returns the next higher value
print(math.floor(2.9)) #it returns the lower value of given value
print(math.e)
print(math.exp(2))
print(math.factorial(5))
print(math.fmod(5,2))
print(math.log(1))
print(math.log10(1))
print(math.log2(2))
print(math.modf(5.3))#sperates real and intergal part
print(math.pi)
print(math.pow(5,3))
print(math.trunc(5.5))'''

#os,sys,random,json.....
#os--->it provides functions to interact with operating system...
'''import os
#print(dir(os))
print(os.getcwd())
#change current directory
os.chdir("/home/workspace/my-project/python_bascis")
print(os.getcwd())
print(os.listdir())
for i in os.listdir():
    print(i)
#print(os.mkdir("sample"))
print(os.removedirs("sample"))

import sys
print(sys.path)#it gives complete root path

#random module---->majorly useful to generate random data
import random,time
#print(dir(random))
#print(random.random())#it gives random number(float)
#otp generation
for i in range(10):
    print(random.randint(1000,9999))
    time.sleep(5) #sleep will be helpful to take time interval
'''
#JSON--->encoding and decoding (josn)---->python objects to json format and viceversa
'''import json
data={'name':'codegnan','age':7}
print(type(data))
parsed_data=json.dumps(data)#while using dumps the data will be converted into string 
print(parsed_data)
print(len(parsed_data))
print(type(parsed_data))
result=json.loads(parsed_data)#while using loads the string  will be converted into original data
print(result)
print(type(result))
sample=json.loads('[12,3,4,5]')
print(type(sample))
'''
#collections--->counter,itertools---->combinations and permutations
'''from collections import Counter
data=['A','B','C','A','A','C']
r=Counter(data)
print(r)
print(type(r))
a=dict(Counter(data))
print(a)
print(type(a))'''



