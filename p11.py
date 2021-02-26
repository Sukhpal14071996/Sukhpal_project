# Program 11: Write a Program to enter the numbers and to print greatest number using loop.

#CODE
import array as ar
arr = ar.array('d', [])
n = int(input("How many numbers you want to enter: "))
print("Enter numbers: ")
for i in range(n):
    arr.append(int(input()))
max_n = arr[0]
for i in range(n):
    if max_n<arr[i]:
        max_n = arr[i]
print("The greatest number is : ", max_n)
        
#OUTPUT