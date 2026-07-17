#sequence types---->list--->mutable, indexed,ordered, heterogenous collection
#nested lists---->list inside another lists
data=['lakshmi','codegnan',['python','genAI','AAI'],3]
print(data)
print(len(data))
print(data[2]) #taking inner list from the data
a=data[2][1][-2:]#want AI from genAI
print(a)
b=data[::3]#getting output as ['lakshmi',3]
print(b)
#append(),extend(),insert()
print(data)
print(len(data))
data.append('RAG')#length will be increased by 1
print(data)
print(len(data))
data.insert(1,'prasanna')##length will be increased by 1
print(data)
print(len(data))
data.extend(('RAG','java'))
print(data)
print(len(data))
#pop(),remove(),index(),count(),clear()
data.pop()
print(data)
data.remove(3)
print(data)
data.index('prasanna')
print(data)
data.count('RAG')
print(data)
data.reverse()
print(data)
data.clear()
print(data)
