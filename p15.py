# Program 15: Write a python function sin(x,n) to calculate the value of sin(x) using its Taylorseries expansion
# up to n terms.

#CODE
import math
n=int(input("Enter n: "))
x=float(input("\nEnter x: "))
def sin(x,n):
    sinx=0
    for i in range(1,n+1,4):
        sinx+= (x**i)/math.factorial(i)
    for i in range(3,n+1,4):
        sinx-= (x**i)/math.factorial(i)
    return(sinx)
print("\nsin(",x,",",n,") = ",sin(x,n))

#OUTPUT