'''performing different types of programs
1.swap
2.fact
'''
#swap
def swap(a,b):
    temp=a
    a=b
    b=temp
    return (a,b)

#fact
def fact(n):

    if n>0:
        if n==0 or n==1:
            return 1
        else:
            return n*fact(n-1)
    else:
        return 'invalid number'


#reverse
def strings(a):
    return a[::-1]

#vowels in string
def vowels(name):
    count=0
    for i in name:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count=count+1
    return count

#fib
def fibonacci(a,b,n):
    if n==0:
        return a
    elif n==1:
        return b
    for i in range (2,n+1):
        c=a+b
        a=b
        b=c
    return c

#title case
def title_case(a):
    return a.title()

#largest numbers
def largest(a,b,c):
    if a>b and b>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c

#remove dupli
def depli(*b):
    return set(b)

#vote
def vote(age):
    if age>=18:
        return ("your age is {} years, eligible".format(age))
    else:
        age=18-age
        return (f"after {age} years you can vote")
        

 





















