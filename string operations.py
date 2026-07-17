#repetition --->we use *
'''data='agent'
print(data*3)'''
#membership-->in, not in
'''print('code' in 'codegnan')
print('agent' not in 'generative AI')
print('agent' in 'generative AI')'''
#Indexing --->we access position of an object in a string,we use[] to the index of an object, it starts with 0 and ends at len(obj)-1
'''name = 'codegnan'
print(len(name))#returns length of the string
print(name[0])#returns first character
print(name[6])#returns 6th index position character
print(name[30])#returns index error 
print('agent'[2])'''
#negative indexing-->starts from last--> -1
'''name='codegnan'
print(name[-1])
print(name[-4])
print(name[4])'''

'''name='agentic ai course'
print(len(name))
print(name[7])
print(name[9])
print(name[-9])
print(name[25])'''

#strings are immutable
'''name='codegnan'
name[5]='p'
#name[5]='p'-->item assignment is not possible
print(name)'''

#slicing-->accessing group of characters-->[start:end] start will be included,end will be excluded
'''name='codegnan'
print(name[ : ])
print(name[1:5])
print(name[ :5])
print(name[4: ])
print(name[4:25])#even though end is of out of range it '''
#negative slicing 
'''name='codegnan'
print(name[-5:])
print(name[:-7])
print(name[-5:-1])#remember lower to higher
print(name[-1:-5])#returns empty string
print(name[:-8])#returns empty sting
print(name[-8:])#returns complete string'''

#[::]-->[start:end:step]-->step= step-1
'''name='codegnan'
print(name[::2])
print(name[::4])
print(name[1:7:3])
print(name[2:9:5])
print(name[:4:5])
print(name[1::4])'''

#negative
'''name='codegnan'
print(name[::-1])#prints in reverse order
print(name[::-2])
print(name[::-6])
print(name[-8:-1:])#returns complete excluding last character
print(name[-8:-1:-2])#returns empty string as no possibilities
print(name[-8:-1:2])
print(name[1:7:-1])#returns empty string'''
#built-in functions-->len(),type(),min(),max(),ord(),chr()
'''place='hyderabad'
places='Hyderabad'
print(len(place))
print(min(place))
print(max(place))
print(min(places))
print(type(place))
print(ord('A'))
print(chr(90))'''

#methods(functions) on strings
#case conversions--> converting from one case to another
#lower(),upper(),title(),capitalize(),swapcase()
course="Agentic ai"
print(course)
print(course.lower())
print(course.upper())
print(course.swapcase())
print(course.title())
print(course.capitalize()) 

























































