'''
oop---->Encasulation, inheritance
#encasulation---->it is also one of the key feature of oop. it actually the attributes(data) and methods (functions) into a whole single unit(class)
it helps to main data integrity,privacy...
Type of attributes using encapsulation:
public--->can be accessible anywhere inside and outside the class
protected---->we wanted to make it for internal use,can be accessible outside the class
private--->hidden,cannot accessible directly
for usage of protected along with private attributes we use underscore notation
'''
#usage of public attributes
'''
class users:
    """usage of public attributes"""
    def __init__(self,name):
        self.name=name #public attribute
    def display(self):
        return f'{self.name} is in AAA batch'
user1=users("lakshmi prasanna")
print(user1.__dict__)
print(user1.display())
user1=users("prasanna")
print(user1.__dict__)
print(user1.display())
'''

#usage of protected attribute
'''
class users:
    """usage of public attributes"""
    def __init__(self,name,_otp):
        self.name=name #public attribute
        self._otp=_otp #protected attribute
    def display(self):
        print(f'{self.name} is in AAA batch')
        print(f'OTP is {self._otp}')
user1=users("Agent",23456)
print(user1._otp)
user1.display()
user1._otp=34567
print(user1.__dict__)
user1.display()
'''
#usage of private attributes
'''
class users:
    """usage of public,protected,private attributes"""
    def __init__(self,name,_otp,password):
        self.name=name #public attribute
        self._otp=_otp #protected attribute
        self.__password=password
    def display(self):
        print(f'{self.name} is in AAA batch')
        print(f'OTP is {self._otp}')
        print(f'Logged in with {self.__password}')
user1=users("lakshmi",23456,"admin123")
print(user1.name)
print(user1._otp)
#print(user1.password)#attribute error
print(dir(user1))
print(user1._users__password)#namemangling
user1.display()
'''
#accessing private attributes using getter and setter methods....
'''
class users:
    """usage of public,protected,private attributes"""
    def __init__(self,name,password):
        self.name=name #public attribute
        self.__password=password
    #accessing private attributs using getter method
    def get_password(self):
        return "******" #here we are accessing
    #using setter method we want to have validations
    def set_password(self,new_password):
        if len(new_password)<6:
            print(f'Error in validating the password,enter atleast 6 characters')
        else:
            self.__password=new_password
            print(f'The password is modified and it is {self.__password}')
user1=users("lakshmi","admin123")
print(user1.get_password())
user1.set_password("123")
user1.set_password("1234567")
print(user1.__dict__)
'''
#accessing protected attributes using getter and setter methods....
'''
class users:
    """usage of public,protected,private attributes"""
    def __init__(self,name,otp,password):
        self.name=name #public attribute
        self._otp=otp
        self.__password=password
    #accessing protected attributs using getter method
    def get_otp(self):
        print(f'{self._otp}') #here we are accessing
    #using setter method we want to have validations
    def set_otp(self,new_otp):
        if len(new_otp)<4:
            print(f'Error in validating the otp,enter atleast 4 characters')
        else:
            self._otp=new_otp
            print(f'The otp is modified and it is {self._otp}')
    #accessing private attributs using getter method
    def get_password(self):
        return "******" #here we are accessing
    #using setter method we want to have validations
    def set_password(self,new_password):
        if len(new_password)<6:
            print(f'Error in validating the password,enter atleast 6 characters')
        else:
            self.__password=new_password
            print(f'The password is modified and it is {self.__password}')
user1=users("lakshmi","1234","admin@123")
user1.get_otp()
user1.set_otp("123")
user1.set_otp("56789")
print(user1.get_password())
print(user1.set_password("123456"))
print(user1.__dict__)
'''
#inheritance---->one of the key principles in oop, which mainly focuses on acquiring the properties from base class(parent class)
#to dervied class(child class)
'''
syntax:
class parent:
    statements(s)....
    .....
class child(parent):
    statements....
    .......
'''
#single inheritance,multiple inheritance,multilevel inheritance,hybrid inheritance
#scenario of usernames creation and updation in profile page
'''
class users:
    """user details"""
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def full_name(self):
        return self.fname+self.lname
#user1=users("lakshmi","prasanna")
#print(user1.full_name())
class update_users(users):
    def update_name(self):
        return self.fname.title().strip()+" "+self.lname.title().strip()
user1=update_users("lakshmi","prasanna")
print(user1.full_name())
print(user1.update_name())
'''
#singal inheritance
'''
users--->parent
update user1(users)-->child1

update user2(users)---->child2
'''
#whatsapp scenario-->users,business users(single inheritance)
class users:
    def send_message(self):
        print(f"message is sending")
    def make_call(self):
        print(f"making a call")
    def send_photo(self):
        print("sending photos")
class business_users(users):
    def send_catlog(self):
        print("catlog is sending")
user1=business_users()
print(dir(user1))
user1.send_message()
user1.send_catlog()

















































































