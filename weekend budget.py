#weekend planner based on budget
Budget=int(input("enter the price:"))
if Budget>10000:
    print("plan:",'Trip')
elif Budget>5000:
    print("plan:",'Resort Stay')
elif Budget>3000:
    print("plan:",'Movie and Dinner')
elif Budget>1000:
    print("plan:",'Cafe and Shopping')
elif Budget>500:
    print("plan:",'Street Food and Park Visit')
else:
    print("plan:",'Stay Home')

#another method
Budget=int(input("enter the price:"))
if Budget>0:
    if Budget>10000:
        print("plan:",'Trip')
    elif Budget>5000:
        print("plan:",'Resort Stay')
    elif Budget>3000:
        print("plan:",'Movie and Dinner')
    elif Budget>1000:
        print("plan:",'Cafe and Shopping')
    elif Budget>500:
        print("plan:",'Street Food and Park Visit')
    else:
        print("plan:",'Stay Home')
else:
    print("invalid Budget")

    
