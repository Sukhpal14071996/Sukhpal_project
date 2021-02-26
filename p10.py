# Program 10: Write a Program to enter the number of terms and to print the Fibonacci Series.

#CODE
n = int(input("How many terms of fibonacci series you want to print : "))
a = 0
b = 1
c = 0
print(n, "terms of the fibonacci series are:\n")
print(a, b, end = " ")
for i in range(n-2):
    c = a+b
    a = b
    b = c
    print(c, end = " ")
#OUTPUT