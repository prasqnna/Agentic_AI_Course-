#tuples-->immutable,ordered,indexed,heterogenous sequence type-->()
'''data=1,24,5
print(data)
print(type(data))'''

#nested tuples and also have lists inside it
'''details=('codegnan',32,(2,4,5),'saketh',[12,45,'agents','rag'])
print(details)
print(len(details))
print(details[2])
print(details[4][2])

#details[0]=details[0].replace('n','f')#tuples are immutable we cant modify it 
#print(details)

details[4][2]=details[4][2].replace('a','A')#here we are using lists so its mutable
print(details)
print(details[1:4])
print(details[::3])

details[4].pop(2)
print(details)'''

#operations on tuples--->indexing,slicing,membership,concatenation/merging,repetition
'''age=22,21,32,25
ids=231,342,213
print(age+ids)
print(age*2)
print(22 in age)'''

#len(),min(),max(),type()
'''age=(25,12,45,65)
print(min(age))
print(max(age))
print(sorted(age))#it will give output as list
print(tuple(sorted(age)))#typecasting'''

#index(),count()
'''details=('saketh','codegnan','Agentic AI',34,23,5.8)
print(details)
print(details.index(34))
print(details.count(34))'''

#tuple--->list....(typesting)
'''details=list(details)
print(details)
print(type(details))'''
#convert string to list/tuple
'''a='codegnan'
print(list(a))
print(tuple(a))'''

#set datatype-->sets,frozen sets
#sets--->set is a unique, mutable collection,unodered --->set()
a={}#by default it is empty dictionary
'''b=set()
print(type(a))
print(type(b))

ids={123,124,125,126,127,123,124}
print(ids)
print(len(ids))'''

#we cant have list and set inside the main set collection 
'''data={'codegnan',32,'saketh',[12,45,'agents','rag']}
print(data)
data={'codegnan',32,'saketh',{12,45,'agents','rag'}}
print(data)'''

#as set is mutable we can insert,remove elements into a set
#add(),update()
ids={123,124,125,126,127,123,124}
print(ids)
'''ids.add(156)
print(ids)
ids.add('agents')
print(ids)
ids.update((170,180))
print(ids)
details=['siva','sam','ram','ajay']
ids.update(details)
print(ids)'''

#remove elements from a set ----> discard(),remove(),clear(),pop()
'''ids.discard(123)
print(ids)
ids.remove(124)
print(ids)
#ids.remove(123)#returns key error
#ids.discard(123)#discard will avoid error
print(ids.pop())#removes and returns an arbitrary element from a set
print(ids.pop())
print(ids.pop())
#print(ids.pop())#it has become empty set
print(ids.clear())
print(ids)'''

#union,intersection,difference,symmetric difference,subsets,supersets
ages={35,23,123,24,25}
print(ages)
'''d=ids.union(ages)
print(d)
e=ids.update(ages)
print(e)
print(ids)
f=ids.intersection(ages)
print(f)
g=ids.intersection_update(ages)
print(g)
print(ids)
k=ids.difference(ages)
print(k)
p=ids.symmetric_difference(ages)#removes common elements and returns elementsv from all sets
print(p)
h=ids.symmetric_difference_update(ages)
print(h)
print(ids)'''
# |(union) , &(intersection), -(difference), ^(symmetric difference)
'''a={1,2,3}
b={1,2,3,4,5}
c=a.issubset(b)
print(c)
d=b.issuperset(a)
print(d)
e=a.isdisjoint(b)
print(e)'''

#frozenset------>immutable set
data=frozenset(ids)
print(data)
print(type(data))

#we cannot insert/remove elements but mathematical operations are possible
details=frozenset([34,35,34,32,31])
print(details)
print(min(details))
print(max(details))
print(sorted(details))


#practice on lists and sets create a nested seque








































































