import miniproject
while True:
    print("1. swap")
    print("2. fact","3. reverse","4.vowels","5.fibonacci","6.title case","7.largest","8.remove duplicates","9.vote")

    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        a=int(input("enter the number:"))
        b=int(input("enter the number:"))
        print(miniproject.swap(a,b))
    elif choice == 2:
        n=int(input("enter the value of n:"))
        print(miniproject.fact(n))
    elif choice == 3:
        a=input("enter the string:")
        print(miniproject.strings(a))
    elif choice == 4:
        name=input("enter the string:")
        print(miniproject.vowels(name))
    elif choice == 5:
        a=int(input("enter the number:"))
        b=int(input("enter the number:"))
        n=int(
            input("enter the n value:"))
        print(miniproject.fibonacci(a,b,n))
    elif choice == 6:
        a=input("enter the sentence:")
        print(miniproject.title_case(a))
    elif choice == 7:
        a=int(input("enter the number:"))
        b=int(input("enter the number:"))
        c=int(input("enter the n value:"))
        print(miniproject.largest(a,b,c))
    elif choice == 8:
        a=input("enter the words:")
        print(miniproject.depli(1,2,3,1,4,5,3,6))
    elif choice == 9:
        age=int(input("enter the age:"))
        print(miniproject.vote(age))
    elif choice==10:
        num = int(input("enter the number:"))
        print(miniproject.numbers(num))
        
    elif choice==11:
        print("Thank you")
        break
    else:
        print("invalid choice")

