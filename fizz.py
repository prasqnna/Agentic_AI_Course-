n=int(input("enter the number:"))
if n>0:
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Buzz")
    else:
        print("not divisible 3 or 5")
else:
    print("enter only positive values")
