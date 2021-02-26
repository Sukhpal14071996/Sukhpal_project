# Program 18: Write a Program to implement Inheritance. Create a class Employee inherit two classes
# Manager and Clerk from Employee.

#CODE
class Employee:
    def __init__(self):
        self.name=""
        self.age=0
    def input(self):
        name=input("Enter the name of employee: ")
        age=int(input("Enter the age of employee: "))
        self.name= name
        self.age= age
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
class Manager(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.title= "Manager"
        self.basic_sal= 0
    def input(self):
        Employee.input(self)
        self.basic_sal= int(input("Enter the basic salary: "))
    def display(self):
        Employee.display(self)
        print("Title: ",self.title)
        print("Basic salary: ",self.basic_sal)
        self.total_salary()
    def total_salary(self):
        bonus=0
        if self.basic_sal>=30000:
            bonus= 0.1*self.basic_sal
        elif self.basic_sal>20000:
            bonus=0.08*self.basic_sal
        print("Total salary of employee is: ",(self.basic_sal+bonus))
class Clerk(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.title= "Clerk"
        self.basic_sal= 0
    def input(self):
        Employee.input(self)
        self.basic_sal= int(input("Enter the basic salary: "))
    def display(self):
        Employee.display(self)
        print("Title: ",self.title)
        print("Basic salary: ",self.basic_sal)
        self.total_salary()
    def total_salary(self):
        bonus=0
        if self.basic_sal>=15000:
            bonus= 0.1*self.basic_sal
        elif self.basic_sal>10000:
            bonus=0.08*self.basic_sal
        print("Total salary of employee is: ",(self.basic_sal+bonus))
while True:
    ch=int(input("1.Manager data\n2.Clerk data\n3.Exit\n"))
    if(ch==1):
        m=Manager()
        m.input()
        m.display()
    elif(ch==2):
        c=Clerk()
        c.input()
        c.display()
    elif(ch==3):
        break
#OUTPUT