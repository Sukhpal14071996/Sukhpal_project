# Program 22: Write a Program to enter multiple values-based data in multiple columns/rows and show that
# data in python using DataFrames and pandas.

#CODE
import pandas as pd
n= int(input("Enter number of columns you want to enter: "))
k= int(input("Enter number of rows you want to enter: "))
data= []
for i in range(k):
    print("Enter row ",i+1," values: ")
    row=[]
    for j in range(n):
        row.append(int(input()))
        data.append(row)
df= pd.DataFrame(data)
print("Data Frame from user values: ")
print(df)
#OUTPUT