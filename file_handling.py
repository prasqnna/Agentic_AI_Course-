#store the data---->files(.txt files)--->open()
#file modes---->'r','w','a'
#default file mode--->open("file_name.txt".'r')#default we have 'r'abs
file=open('example.txt')
#print(file)
#print(file.read())#returns entrie text from the file
#print(file.read(10))#we can also mention the size
#print(file.readlines())#returns in list
#a=file.readlines()
#print(len(a))
#print(file.readline())#returns single line from the file



#check weather the file exists or not
import os
'''
if os.path.exists('example.txt'):
    f=open("example.txt").read()
    print(f)
    print(f"file is already present")
else:
    print(f"file not found")
    

#checking the file and its size
file_path="example.txt"
if os.path.exists(file_path):
    print(f'File size is {os.path.getsize(file_path)}bytes')
    print(f'File absolute path is {os.path.abspath(file_path)}')
else:
    print("file not found")
    '''
#'w' mode---->it will automatically creates a file and if same file name is present it will overrides the content in previous file
'''a=open("agents.txt",'w')
print(a)
a.write("AA-HYD-001 students are good and cool.")
a.write("\nyes it is True")
a.writelines("\nAgentic AI is the big thing happening.the world is progressing")

#if the file is already present 'w' mosde overrides the context
file=open('example.txt','w')
file.write("Agentic AI is the big thing happening.the world is progressing")
file.close()
#we can use with statement
with open("example.txt",'w') as file:
    print(file)
    file.writelines("Agentic AI is the big thing happening.the world is progressing.")
    #no need to mention close()


#'a' append mode holds the same content in the existing file
with open("example.txt",'a') as f:
    print(f)
    f.write("\n pthon ahents rag")
    
with open ('rag.txt','a') as r:
    print(r)
    r.writelines("Agents,MCP,RAG,GEN AI....")

with open('rag.txt','r+') as d:
    print(d.read())
    d.write('\n Claude,ChatGPT,Copilot....')

import os
d=os.listdir()#returns list of all directories
for file in d:
    if file.endswith('.txt'):
        print(file)
        '''
#exception handling--->program(try,except,finally)
'''
syntax:
try:
    base statements(s) which may raise error.....
    ......
except Exception (error name) as e:
    ......
finally:
    statements(s).....

#type error,value error,index error,arithmetic error,zerodivision error,attribte error

try:
    a,b=map(int,input("enter the values").split(","))
    result=a/b
    print(f'result is {result}')
except ZeroDivisionError:
    print("denominator can not be zero")
except ValueError:
    print('values to be only integers')
finally:
    print("anyways this will be printed")
'''
try:
    a,b=map(int,input("enter the values").split(","))
    result=a/b
    print(f'result is {result}')
except (ZeroDivisionError,ValueError) as e:
    print(f'the error occured {e}')
finally:
    print("anyways this will be printed")
