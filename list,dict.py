'''Type conversions--->list,tuple,set,dict
list--->str,tuple,set,dict
'''
'''age=[23,21,43]
print(type(age))
b=str(age)
print(b)
print(type(b))
e=tuple(age)

c=dict.fromkeys(age)
print(c)'''


#str---->list,tuple,dict
'''name='codegnan'
print(type(name))
g=list(name)
print(g)
h=name.split()
print(h)
j=name.split(",")
print(j)
e=dict.fromkeys(name)
print(e)'''

#input formating---->list input,tuple input,dict input---->eval()
#list as input
'''data=eval(input("enter the list:"))
print(data)
print(type(data))
details=eval(input("enter the tuple:"))
print(details)
print(type(details))
data=eval(input("enter the dict:"))
print(data)
print(type(data))'''



#repetition statements(loops)---->for,while
#loops will automate the tasks
'''
for loop is used to iterate items in a collection (str,list,tuple,set,dict) also can generate a sequence of numbers(range)
syntax for:
for <loop_var> in collection/range_function:
statements(s)....
'''
'''marks=[24,25,21,20]
for mark in marks:
    print(mark)
    print(mark,end='\t')
#find the sum and average of marks
marks=list(map(int,input("enter the marks:").split()))
summ=0;avg=0
for i in marks:
    summ=summ+i
print(summ)
print(f'sum of the given values is {summ}')
avg=(summ)/len(marks)
print(f'average of the given values is {avg}')


details={'names':['sai','abhi','ram'],
         'marks':[24,20,28]}
print(details.items())
for key in details:
    print(key)
for value in details.values():
    print(value)
for key,value in details.items():
    print(f'key is {key}')
    print(f'value is {value}')'''
    


'''#range(start,end,step)--->generates a sequence of values
#range(end) #by default start is 0
for i in range(5):
    print(i)
    print(f'value of i is {i}')
#range(start,end)
for i in range(1,11):
    print(i,end=' ')

#range(start,end,step)
for i in range(1,11,2):
    print(i)

for i in range(10,-1,-2):
    print(i)

#home task
Ord('A')
#A B C D E F G H
#h f d b

#daily workout log ----> fitness streak
#longest streak
work_log=[1,1,1,0,1,1,0]
longest_streak=0
current_streak=0
for i in work_log:
    if i==1:
        current_streak+=1
    else:
        break
longest_streak=current_streak
print(longest_streak)'''

#A B C D E F G H
print(ord('A'))
print(ord('H'))
for i in range(65,73):
    print(chr(i),end=' ')

#h f d b
print(ord('h'),end='\n')
print(ord('b'))
for i in range (104,97,-2):
    print(chr(i),end=' ')






























































