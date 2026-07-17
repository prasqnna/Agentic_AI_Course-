#operations on strings
#case conversations,searching,validation(boolean value)
#searching and finding methods-->find(),index(),count()
place= 'Hyderabad'
'''print(len(place))
print(max(place))
print(ord('A'))
print(ord('a'))
print(place)'''

#find()#first occurance of given character
'''print(place.find('d'))#it returns first occurance-->2
print(place.find('a'))
print(place.find('Z'))#if unmacthed char is present it returns -1'''

'''print(place.find('d',3))#we can give the start index for a repeating char to find next position
print(place.find('a',6))'''

#rfind()---> will give last occurance
'''print(place.rfind('d'))
print(place.rfind('w'))#it returns -1 as no character'''

#index()
'''print(place.index('e'))#it returns given char position
print(place.index('d'))
print(place.index('d',3))
#rindex()--->returns the last matching position
print(place.rindex('d'))
print(place.rindex('z'))#raises error'''

#count()-->returns the number of occurances

'''print(place.count('d'))
print(place.count('d',3))#it returns 1 as we has given the spefice index to start
print(place.count('q'))#it return 0'''

#testing methods-->return boolean value
'''print(place.isupper())#returns true if complete string is in uppercase
print(place.islower())
print(place.isalpha())#returns true for an alphabetic string
print('code123'.isalpha())#returns flase as it is alnum string
print('code123'.isalnum())#returns ture as it is alnum string
print('12345'.isalnum())
print('12345'.isdigit())
print(place.startswith('H'))
print(place.startswith('d'))
print(place.startswith('d',2))
print(place.endswith('d'))
print(place.istitle())
print('Agentic ai'.istitle())'''


#space removal (trimming) methods--->strip(),lstrip(),rstrip()
#strip()-->removes both leading and trailing spaces
'''data=' codegnan '
f=data.strip()
print(len(f))
print(f)
a=data.lstrip()#removes leading space
print(len(a))
print(a)
b=data.rstrip()#removes trailing(last) space
print(len(b))
print(b)'''

#replace(),split(),join()
'''b=place.replace('e','f')
print(b)
c='codegnan agentic ai'.replace('a','p')
print(c)
c='codegnan agentic ai'.replace(' ','')#we arereplacing space with empty string
print(c)'''

#split()
'''d='code,python,ai'
print(len(d))
d='code,python,ai'.split(',')#returns list as result but uses given separator
print(d)
print(len(d))'''

#join()--->joins elements with given sep
'''a='code'
b='gnan'
c=a.join(b)
print(c)
print('#'.join('code'))
print('$$'.join('#'))'''

#sequence datatypes-->List[]---->mutable,ordered,indexed,heterogenous

'''age=[21,20,22,32]
print(age)
print(type(age))
print(len(age))

details=['saketh',32,'python',3.45]
print(len(details))
print(type(details))
print(details[2])
print(details[-3])

#we need to extract 'hon' from above list
print(details[2])
print(details[2][3:])
print(details[::-1])
print(details[2:])'''


#indexing and slicing to be worked out............
#output-->['saketh','python']
#output--->[32,3.45]
details=['saketh',32,'python',3.45]
print(details[0:4:2])
print(details[1:4:2])
age=[21,20,22,32]
print(age+details)
print(age*2)
print((age*2)+details)
print(sorted(age))
#print(sorted(age+details))#type error




































































                   
      
