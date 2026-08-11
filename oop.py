'''
tokens-->datatypes--->control flow---->functions--->modules---->(POP)
procedural oritennted programming--->functions

object oriented programming---->objects---->it organizes the data and makes use of it and use in objects
an object is real world entity---->attributes(data),menthod(behaviour) functions


class Class_name:
    attributes....(variables)
    ...........
    ........
    def fname(self):#behaviour
        """doc string"""
        ......
        ......
obj=class_name()....

wooden chair---->chair is an object,class(blueprint which includes complete measurement dimensions)
carpenter--->user,scrap,materials,wood--->memory
resuablity,modularity,abstraction,encapsulation,inheritance,polymorphism

class Product:
    """simple class demonstraction with ecommerce example"""
    platform="Amazon" #class attribute
    def display_product(self):
        print(f"displaying products")
    def stock_available(self):
        print(f"stock is available")
laptop=Product()
print(dir(laptop))
print(laptop.platform)
laptop.display_product()
laptop.stock_available()
mobile=Product()
mobile.display_product()
#product----->class,platform---->attribute,display_product,stock_available---->methods...

class Product:
    """usage of class with instance attributes"""
    platform="Amazon"
    def store_products(self,name,price):
        self.name=name
        self.price=price
    def display_product(self):
        print(f'product name is {self.name}')
        print(f'product price is {self.price}')
mobile=Product()
print(dir(mobile))
mobile.store_products("Iphone",55000)
print(mobile.name)
print(mobile.price)
mobile.display_product()
mobile2=Product()
mobile2.store_products("One plus",35000)
mobile2.display_product


class Product:
    """usage of class with instance attributes"""
    platform="Amazon"
    def store_products(lakshmi,name,price):
        lakshmi.name=name
        lakshmi.price=price
    def display_product(lakshmi):
        print(f'product name is {lakshmi.name}')
        print(f'product price is {lakshmi.price}')
mobile=Product()
print(dir(mobile))
mobile.store_products("Iphone",55000)
print(mobile.name)
print(mobile.price)
mobile.display_product()
mobile2=Product()
mobile2.store_products("One plus",35000)
mobile2.display_product


class Product:
    """usage of class with instance attributes"""
    platform="Amazon"
    def store_products(self,name,price):
        self.name=name
        self.price=price
    def display_product(self):
        print(f'product name is {self.name}')
        print(f'product price is {self.price}')
for i in range(3):
    name=input("enter the name")
    price=int(input("enter the price"))
    mobile = Product()
    mobile.store_products(name,price)
    mobile.display_product()

class Students:
    """students details"""
    batch="AAA-HYD-001"
    def student_data(self):
        self.name=input("enter the name:")
        self.age=int(input("enter the age:"))
        self.place=input("enter the place:")
    def details(self):
        print(f'student name is {self.name}')
        print(f'student is from {self.place} with age as {self.age} years old')
stud1=Students()
print(stud1.batch)
stud1.student_data()
stud1.details()
print(stud1.__dict__)
print(stud1.__doc__)
print(stud1.__class__)
stud2=Students()
print(stud2.batch)
stud2.student_data()
stud2.details()
print(stud2.__dict__)
'''
class Students:
    """students details"""
    batch="AAA-HYD-001"
    def __init__(self,name,place,age):
        """constructor usage"""
        self.name=name
        self.place=place
        self.age=age
    def details(self):
        print(f'student name is {self.name}')
        print(f'student is from {self.place} with age as {self.age} years old')
stud1=Students("lakshmi","hyd",21)
stud1.details()
stud2=Students(place="vizag",name="prasanna",age=21)
stud2.details()





