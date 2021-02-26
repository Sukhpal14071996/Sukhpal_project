# Program 16: Write a Program to determine EOQ using various inventory models.

#CODE
class Inventory():
    def __init__(self):
        self.option=int(input("""Enter model number you want to analyse:
        1: Model 1 (Economic Order Quantity)
        2: Model 2 (Finite Replenishment)
        3: Model 3 (Shortages allowed and fully backlogged)
        4: Model 4 (Generalised Economic Lot Size\n"""))
    def input(self):
        self.A=int(input("Enter per order cost, A (in Rs.): "))
        self.L=int(input("Enter annual demand (# of units): "))
        self.I=int(input("Enter inventory carrying charge per unit per year, Ic (in Rs.): "))
    def model1(self):
        self.Q=(2*self.A*self.L/self.I)**0.5
        self.C=(2*self.A*self.L*self.I)**0.5
    def model2(self,R):
        self.Q=((2*self.A*self.L/self.I)*(R/(R-self.L)))**0.5
        self.C=((2*self.A*self.L*self.I)*((R-self.L)/R))**0.5
    def model3(self,S):
        self.Q=((2*self.A*self.L/self.I)*(S+self.I)/S)**0.5
        self.C=((2*self.A*self.L*self.I)*S/(S+self.I))**0.5
    def model4(self,R,S):
        self.Q=((2*self.A*self.L/self.I)*(S+self.I)/S * (R/(R-self.L)))**0.5
        self.C=((2*self.A*self.L/self.I)*S/(S+self.I) * ((R-self.L)/R))**0.5
    def display(self):
        print("\nOptimal Order Quantity, Q*= ",self.Q)
        print("\nTotal Cost at optimal quantity, K(Q*)= ",self.C)
a=Inventory()
a.input()
if(a.option==1):
    a.model1()
    a.display()
if(a.option==2):
    R=int(input("Enter replenishment rate: "))
    a.model2(R)
    a.display()
if(a.option==3):
    S=int(input("Enter shortage cost: "))
    a.model3(S)
    a.display()
if(a.option==4):
    R=int(input("Enter replenishment rate: "))
    S=int(input("Enter shortage cost: "))
    a.model4(R,S)
    a.display()
#OUTPUT