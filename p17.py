# Program 17: Write a Program to determine different characteristics using various Queuing models.

#CODE
import math
class Queueing():
    def __init__(self):
        self.option=int(input("""Enter model number you want to analyse:
        1: M/M/1 ( Single server model )
        2: M/M/C ( C servers )
        3: M/M/inf ( Self-service ) \n"""))
    def input(self):
        self.l=int(input("Enter arrival rate: "))
        self.u=int(input("Enter departure rate: "))
        self.rho= self.l/self.u
    def model1(self):
        self.L= self.rho/(1-self.rho)
        self.Lq= (self.rho**2) / (1 - self.rho)
        self.W= 1/(self.u - self.l)
        self.Wq= self.rho**2/(self.l*(1 - self.rho))
    def model2(self):
        self.c=int(input("Enter number of servers: "))
        self.k=0
        for i in range(self.c):
            self.k+= self.rho**i/math.factorial(i) #here rho is just lambda/u
        self.k+= ((self.rho**self.c)/math.factorial(self.c))*(1/(1-(self.rho/self.c)))
        self.po=1/self.k #traffic intensity is rho/c
        self.Lq= ((self.rho**self.c)*self.po*(self.rho/self.c))/(math.factorial(self.c)*((1-(self.rho/self.c))**2))
        self.Wq= self.Lq/self.l
        self.L= self.Lq + self.l/self.u
        self.W= self.Wq + 1/self.u
    def model3(self):
        self.L= self.rho
        self.W= 1/self.u
        self.Wq= 0
        self.Lq= 0
    def display(self):
        print("\nExpected number of customers in system: ",self.L)
        print("\nExpected number of customers in queue: ",self.Lq)
        print("\nExpected waiting time for customer in system: ",self.W)
        print("\nExpected waiting time for customer in queue: ",self.Wq)
a=Queueing()
a.input()
if(a.option==1):
    a.model1()
    a.display()
elif(a.option==2):
    a.model2()
    a.display()
elif(a.option==3):
    a.model3()
    a.display()
#OUTPUT