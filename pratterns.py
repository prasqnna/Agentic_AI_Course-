<<<<<<< HEAD
'''
#nested loops--->a loop placed inside another loop---->patterns generations...
syntax:
for i in range(outer_loop):
    for j in range(inner_loop):
        statements.....for every outer loop inner loop will be completely executed
        ..........outer loop---->rows,inner loop---->columns

for i in range(3):
    for j in range(2):
        print(f'value of i is {i},value of j is{j}')
        print(i,j)
for i in range(2):
    for j in range(4):
        print(i,j)
        

for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
    print()
    
    
for i in range(1,4):
    for j in range(1,4):
        print(i,end=' ')
    print()
    
#print(ord('A'))
for i in range(65,68):
    for j in range(1,4):
        print(chr(i),end=' ')
    print()

num=1
for i in range(1,4):
    for j in range(1,4):
        print(num,end=' ')
        num=num+1
    print()
    
for i in range(1,4):
    for j in range(1,4):
        print("*",end=' ')
    print()
    
for i in range(1,4):
    for j in range(1,5):
        print("*",end=' ')
    print()

n=5
for i in range(1,n):
    for j in range(i):
        print("*",end=' ')
    print()
    
n=5
=======
'''n=5
>>>>>>> de5c938 (python materials)
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=' ')
    print()
<<<<<<< HEAD
    
=======
>>>>>>> de5c938 (python materials)
n=1
for i in range(5):
    for j in range(i):
        print(n,end=' ')
        n=n+1
    print()
    
n=65
for i in range(5):
    for j in range(i):
        print(chr(n),end=' ')
        n=n+1
<<<<<<< HEAD
    print()
    

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
    

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()
    
=======
    print()'''



>>>>>>> de5c938 (python materials)
n=5
for i in range(1,n+1): 
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end='')
        else:
            print("*",end=" ")
    print()
<<<<<<< HEAD
'''
=======

>>>>>>> de5c938 (python materials)
n=5
for i in range(1,n): 
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end='')
        else:
            print("*",end=" ")
    print()
for i in range(n,0,-1): 
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end='')
        else:
            print("*",end=" ")
    print()
<<<<<<< HEAD
=======









    
    















>>>>>>> de5c938 (python materials)
    






