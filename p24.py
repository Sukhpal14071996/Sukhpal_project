# Program 24: Write a program to plot a bar chart in python to display the result of a school for five consecutive
#years.
#CODE
import matplotlib.pyplot as plt
year = [2015, 2016, 2017, 2018, 2019]
result = [79.5, 82, 76.7, 92.2, 88.7]
plt.bar(year,result)
plt.title('School result for five consecutive years')
plt.xlabel('Years')
plt.ylabel('Result')
plt.ylim(50,100)
plt.show()

#OUTPUT