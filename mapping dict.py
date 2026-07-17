#mapping ===>dictionary(dict())
#dictionary----->collection of key-value pairs,mutable,ordered....{},dict()
'''details={}
print(details)
print(type(details))
details={'name':'codegnan','place':'hyd','age':7}
print(details)
print(len(details))

#accessing keys
print(details['name'])
print(details['age'])
#print(details['Age'])#keyerror
#keys must be unique in a dictionary
data={'Age':25,'name':'code','Age':26}
print(data)#here recent update value of age will be taken
#in dictionary we index by using keys'''

#create sictionaries using other datatypes
student_data={'ids':[23,21,45,52],
              'name':['praneeth','abhiram','vasanthi','akshitha'],
              'place':('hyd','vjwda'),
              'gender':{'male','female'}}
print(len(student_data))
'''print(student_data.keys())#return keys from dictionary
print(student_data['name'])
print(student_data.values())
student_data['course']=['PFS','JFS','AAA','DA']
print(student_data)
print(type(student_data))
print(type(student_data['ids']))
#now if we want to insert 3 more unique ids
#student_data['ids]=23,45,67#this is not recommended in this case
#print(student_data)
student_data['ids'].extend([56,67,87])
print(student_data)
student_data['name'].insert(1,'ashok')
print(student_data['name'])


#we want to insert new place
student_data['place']=list(student_data['place'])
print(student_data['place'])
print(student_data['course'][1::2])
del student_data['ids'][1:3]
print(student_data['ids'])
student_data['name'].sort()
print(student_data['name'])'''

#keys(),values(),items()
print(student_data.items())#returns key value pairs as tuple
#get will return value if key is existing ,else defult--->none
print(student_data.get('branch'))
print(student_data.get('branch','CSE'))
print(student_data.get('name'))
#print(student_data['branch'])#raises keyerror  as we dont have branch
#set.default()
print(student_data.setdefault('ids'))
#student_data.setdefault('branch')
#print(student_data)
student_data.setdefault('branch',['CSE','CSD','ECE','IT'])
print(student_data)

#update(),pop(),popitem(),clear()
student_data.update({'fees:':[45000],'marks':[45,78,85]})
print(student_data)
print(student_data.pop('marks'))
print(student_data)
print(student_data.popitem())
print(student_data)

#fromkeys() will create a new dictionary by accpeting each object in the given iterable as key where as value is set to none
ids=[23,45,67]
#to convert above list to dictionary
d=dict.fromkeys(ids)
print(d)
d[23]='random'
print(d)
#print(d+d)#not possible for sets and dicts
#membership---->in, not in(keys)
print(23 in d)#returns true as we have 23 as key

#nested sictionaries
data={
    's1':{'id':23,
          'name':'ram',
          'place':'hyd'}
    's2':{'id':24,
          'name':'prasanna',
          'place':'knl'}}
print(data.keys())
print(data.['s1']['name'])

























































      




















