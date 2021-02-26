# Program 21: Write a program to perform read and write operation with .csv file.

#CODE
import csv
import pandas as pd
with open('WriteData.csv',mode='w') as file: #WRITE
    writer= csv.writer(file,delimiter=',')
    writer.writerow(['Programming Language','Designed by','Appeared','Extension'])
    writer.writerow(['Python','Guido van Rossum','1991','.py'])
    writer.writerow(['Java','James Gosling','1995','.java'])
#METHOD 1 for reading
with open('WriteData.csv',mode='r') as csvfile:
    csvreader= csv.reader(csvfile)
    for row in csvreader:
        print(row)
#METHOD 2 for reading
result= pd.read_csv('WriteData.csv')
print(result)
#OUTPUT