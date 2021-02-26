# Program 5: Write a menu driven Program to enter the number and print whether the number is
# a. odd or even
# b. prime.

#CODE
import math
def odd_or_even(n):
    if n%2==0:
        return "an even number"
    else:
        return "an odd number"

def is_prime(n):
    k=0
    for i in  range(2, int(math.sqrt(n))):
        if n%i == 0:
            k=1
            break
    if k==0:
        return "a prime number"
    else:
        return "not a prime number"
            
y = "y"
while(y=="y" or y=="Y"):
    n = int(input("Enter number: "))
    ch = int(input("Enter: \n1: Odd or Even\n2: Prime"))
    if ch == 1:
        print("Given number", n, "is", odd_or_even(n))
    elif ch == 2:
        print("Given number", n, "is", is_prime(n))
    else:
        print("Enter correct choice ...")
    y = input("Press y to continue : ")
#OUTPUT