class student:
    platform="codegnan"
    def __init__(self):
        self.name=input("enter name:")
        self.roll_no=input("enter roll namunber:")
        self.marks=int(input("enter the marks:"))
      
    def display_details(self):
        print(f'student name is {self.name}')
        print(f'roll number is {self.roll_no}')
        print(f'marks gained is {self.marks}')
stud1 = None

while True:
    print("\n1. Students details")
    print("2. Display")
    print("3. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        stud1 = student()
        print(student.platform)

    elif ch == 2:
        if stud1 is not None:
            stud1.display_details()
        else:
            print("Please enter student details first.")

    elif ch == 3:
        print("Exit")
        break

    else:
        print("Invalid choice")
        

    
    
