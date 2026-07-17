data=['lakshmi','prasanna',23,(34,99,78),{'python','java','rag','genai'},{'ML','DL','python'},90,100]
print(data)
print(type(data))
print(len(data))
print(data[3])#getting tuple from the data
print(data[4])#getting set from the data
a=data[1:3]#getting 'prasanna',23 from data
print(a)
b=data[::2]#getting string,int,set from data
print(b)
c=data[0][:4]#getting laks from data
print(c)
data[1]=32
print(data)#changing the value 23 to 32
data[2]=['rag','mcp']#changing prasanna with  the given data 
print(data)
print(len(data))#length will not be changed
data.pop()
print(data)
data[2].remove('rag')
print(data)
print(data[2].index('mcp'))
print(data.count('lakshmi'))
print(data[3][::2])#getting 34,78 from tuple
print(min(data[3]))
print(max(data[3]))
print(tuple(sorted(data[3])))
print(data[3].index(99))
print(78 in data[3])
print(28 in data[3])#checking the given number is present in the tuple or not
print(data[3].count(99))
print(type(data[3]))#checking the type of data
#sets
print(data[4])
print(data[5])
data[5].add('java')
print(data[5])
data[4].update(('MCP','read'))
print(data[4])
print(data)
data.pop()
print(data)
data.pop(1)
print(data)
g=data[3]|(data[4])
print(g)
B=data[3].intersection(data[4])
print(B)
C=data[3].intersection_update(data[4])
print(data[3])
D=data[4].difference(data[3])
print(D)
E=data[3].difference_update(data[4])
print(data[3])
F=data[3].symmetric_difference(data[4])
print(F)
G=data[3].symmetric_difference_update(data[4])
print(data[3])
Z=data[4].issubset(data[3])
print(Z)
V=data[3].issuperset(data[4])
print(V)
r=data[3].isdisjoint(data[4])
print(r)
print(data[3].pop())
data[4].remove('ML')
print(data[4])
data[3].discard('genai')
print(data[3])
#frozenset
O=frozenset(data[3])
print(O)
print(type(O))
#type casting
print(data)
C=list(data[2])
print(C)
d=data.copy()
print(d)
d[1][0]='GENAI'
print(d)
print(data)
data.reverse()
print(data)
data.append('genai')
print(data)
data.extend(('ml','dl'))
print(data)
