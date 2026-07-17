#sequence types-->list-->mutable,indexed,ordered, heterogenous collection
#nested lists--->list inside another lists
'''data=['codegnan',35,5.56,['python','java','AAI','DA'],100,45]
print(data)
print(len(data))
#we need to access inner list as below
print(data[3])
#now i want to get 'python' and 'java' from above list
a=data[3][:2]
print(a)
b=data[3][2:]
print(b)
#get only 'pyt' as output
c=data[3][0][:3]
print(c)
#get only 'ava' as output
d=data[3][1][1:]
print(d)
#get the output as ['python','AAI']
e=data[3][::2]
print(e)
#get the output as [35,['python','java','AAI','DA'],45]
f=data[1::2]
print(f)'''

#Lists are mutable---->we can insert/remove elements 
'''data=['codegnan',35,5.56,['python','java','AAI','DA'],100,45]
#using indexing and slicing-->change
#35-->45
data[1]=45
print(data)
print(len(data))
data[2]=['Agents','prompt','RAG']
print(data)
data[3][1]='rag'
print(data)
#indexing will never change the length of the collection
'''

#now we will slicing
data=['codegnan',35,5.56,['python','java','AAI','DA'],100,45]
'''data[1:3]=['java','DSA']
print(data)
data[1:3]=['RAG','MCP','Agents','Lora','GPT','Sonet']
print(data)
data[3][1::2]=['RAG','MCP']
print(data)

#indexing,slicing,striding can insert elements but we loose our original data
'''

#append(),extend(),insert()
#append()--->inserts only single object at the end of list/empty list we can start assing the objects to it
#length will be incrementally increased
details=['saketh',32,'codegnan']
'''print(len(details))
print(details)
details.append(34)
print(details)
details.append('agentic AI')
print(details)
details.append(data)
print(details)
print(details.append("saketh"))#it returns none as we need to print only list
print(details)'''

'''age=[]
age.append(3)
age.append(4)
age.append(5)
print(age)'''

#extend()--->inserts multiple objects(iterable) to the end of the list
#details.extend(34,35)#type error
#print(details)
'''details.extend((34,35))
print(details)
details.extend('codegnan')#it slipts into charcters 
print(details)
details.extend(['codegnan'])
print(details)
details.append(data)
print(details)
print(len(details))'''

'''details.extend(data)
print(details)
print(len(details))'''

#insert()--->inserts obeject before object
'''details.insert(1,'Python')
print(details)
print(len(details))
details.insert(5,'agents')
print(details)
details.insert(6,['temp','agents'])
print(details)
details.insert(-2,'ai')
print(details)

details[-1].append('AAA')
print(details)
details[-1].extend(['RAG','MCP'])
print(details)
details[-1].insert(1,'claude')
print(details)'''

#pop(),remove(),clear()
#pop()--->removes by default last index if not given 
'''details=['saketh',32,'codegnan']
details.extend(['agents','MCP'])
print(details)
details.pop()
print(details)
details.pop(1)
print(details)
#remove()
details.remove('agents')#removes first occurance of a value 
print(details)
#clear()
details.clear()#removes all objects in the collection and returns empty list
print(details)
#to extract group of objects---->del
del details[2:4]
print(details)'''

#index(),count(),copy(),sort(),reverse()
'''details.extend(['agents','rag'])
print(details)
print(details.index('agents'))
print(details.index('agents',4))
print(details.count('agents'))
print(details.count('qwerty'))'''
#print(details.index('qwerty'))#value error
#details.sort()
#print(details)
'''details.pop(1)
print(details)
details.sort()
print(details)'''
b=[12,-98,23,78,2]
'''b.sort()
print(b)
b.sort(reverse=True)
print(b)
b.reverse() #b[::-1]
print(b)'''


#copy()---->creats a shallow copy of list
'''c=b.copy()
print(c)
c[2]='codegnan'
print(c)
print(b)'''

#create nested list and observe copy() in it
data=['lakshmi','prasanna',['python','RAG','AAI'],'codegnan','python']
d=data.copy()
print(d)
print(data)
d[3]='java'
print(d)
d[2][1]='GENAI'
print(d)
print(data)













































            































































































