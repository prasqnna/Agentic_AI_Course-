'''
OOP-->Encapsulation,Inheritence

#Encapsulation-->It is also one of the key feature of OOP.It actually bundle the attributes(data) and
methods(functions) into a whole single unit(class) it helps to main data integrity,privacy..

Type of Attributes using Encaosulation:
Public-->can be accessible anywhere inside and outside the class

protected-->we wanted to make it for internal use,can be accessible outside of the class
Private-->hidden,cannot accessible directly
For usage of Protected along with private attributes we use underscore notation

#Usage of public Attributes
class Users:
    """Usage of public Attributes"""
    def __init__(self,name):
        self.name=name#Public attribute
    def display(self):
        return f'{self.name} is in AAA batch'

user1=Users("saketh kallepu")
print(user1.__dict__)
print(user1.display)
user1=Users("Saketh")
print(user1.display())
print(user1.__dict__)

class Users:
    """Usage of public Attributes"""
    def __init__(self,name,_otp):
        self.name=name#Public attribute
        self._otp=_otp#protected attribute
    def display(self):
        print(f'{self.name} is in AAA batch')
        print(f'OTP is {self._otp}')

user1=Users("Agent",23456)
print(user1._otp)
user1.display()
user1._otp=34567
print(user1.__dict__)
user1.display()

class Users:
    """Usage of public Attributes"""
    def __init__(self,name,_otp,password):
        self.name=name#Public attribute
        self._otp=_otp#protected attribute
        self.__password=password
    def display(self):
        print(f'{self.name} is in AAA batch')
        print(f'OTP is {self._otp}')
        print(f'Logged in with {self.__password}')
user1=  Users("saketh",23456,"admin123")
print(user1.name)
print(user1._otp)
#print(user1.password)#Attribute error
print(dir(user1))
print(user1._Users__password)#NameMangling
user1.display()

#Accessing Private Attributes using getter and setter methods..
class Users:
    """Usage of public Attributes"""
    def __init__(self,name,password):
        self.name=name#Public attribute
        self.__password=password#Private attribute

    #Accessing Private attribute using getter method
    def get_password(self):
        return "******"#here we are accessing

    #using Setter Method we want to have validations
    def set_password(self,new_password):
        if len(new_password)<6:
            print(f'Error in validating the passworde=,enter atleast 6 charachters')
        else:
            self._password=new_password
            print(f'The password is modified and it is {self.__password}')
user1=Users("saketh","admin123")
print(user1.get_password())
user1.set_password("123")#validation
user1.set_password("qwerty123")
print(user1.__dict__)

#create a scenario for protected attributes use getter() and setter()
class Users:
    """Usage of public Attributes"""
    def __init__(self,name,otp):
        self.name=name#Public attribute
        self._otp=otp#Private attribute

    #Accessing Private attribute using getter method
    def get_otp(self):
        return self._otp#here we are accessing

    #using Setter Method we want to have validations
    def set_otp(self,new_otp):
        if len(new_otp)<6:
            print(f'Error is validating OTP')
        else:
            self._otp=new_otp
            print(f'The otp is modified and it is {self._otp}')
user1=Users("saketh",123456)
print(user1.get_otp())
#User1.set_otp()#validation
user1.set_otp("567893")
print(user1.__dict__)'''


#Inheritence-->One of the key principle in OOP,which mainly focuses on
#acquiring the properties from base class(parent class)
#to derived class(child class)
'''
Syntax for inheritence

class Parent:
     statement(S)...
class Child(Parent)
     statement(s)....
     .....
'''

#single inheritence,multiple inheritence,multilevel inheritence,Hybrid inheritence

#scenario of usernames creation and updation in profile page

class Users:
    """User details"""
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def full_name(self):
        return self.fname+self.lname
user1=Users("vasanthi","kalavakuri")
print(user1.full_name())
class Update_Users(Users):
    def update_name(self):
        return self.fname.title().strip()+" "+self.lname.title().strip()
user1=Update_Users("vasanthi","kalavakuri")
print(user1.full_name())
print(user1.update_name())


#Single inheritence
'''
Users-->Parent

Update User1(Users)--child1

Update User2(Users)-->child2
'''

#Whatsapp scenario-->Users,business Users(Single Inheritence)
class Users:
    def send_messages(self):
        print("message is sending")
    def make_voicecall(self):
        print("voice call is ringing")
    def make_videocall(self):
        print("video callm is ringing")
    def send_videos(self):
        print("videos are sending")
class Business_users(Users):
    def send_catlog(self):
        print(f'send catalog')
user1=Business_users()
print(dir(user1))
user1.send_messages()
user1.send_catlog()

































            





















    
