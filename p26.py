# Program 26: Write a program in python to plot a pie chart on consumption of water in daily life.

#CODE
import matplotlib.pyplot as plt
labels=['Bath','Toilet','Dishwasher','Washing Machine','Water Wastage','Car Washing']
size=[38,17,12,10,5,18]
plt.pie(size,labels=labels,autopct='%0.0f%%')
plt.show()
#OUTPUT