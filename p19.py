# Program 19: Program to fit Poisson distribution on a given data. 

#CODE
import pandas as pd
from scipy.stats import poisson
import matplotlib.pyplot as plt
from scipy.stats import chisquare
#FITTING DATA
data=pd.read_csv('poisson_data.csv')
print(data)
data['fixi']=data.Interval*data.Frequency
lamda=data.fixi.sum()/data.Frequency.sum()
print("Sample mean, estimate of lambda= ",lamda)
print("Total obs frequency, N= ",data.Frequency.sum())
data['P[Xi]']= poisson.pmf(data.Interval,[lamda]*len(data.Interval))
data['Expected Frequency']=data.Frequency.sum() * data['P[Xi]']
print(data)
#PLOTTING DATA
ax=plt.gca()
data.plot(kind='bar',x='Interval',y='Frequency',ax=ax)
data.plot(kind='line',x='Interval',y='Expected Frequency',ax=ax)
plt.show()
#GOODNESS OF FIT TEST
print("Ho: there is no significant difference between observed and expected frequencies")
print("H1: there is a significant difference between observed and expected frequencies")
chi,p=chisquare(data.Frequency,data['Expected Frequency'])
print("test statistic, chisq= ",chi)
print("p-value= ",p)
if(p>0.05):
    print("Since p-value>0.05, we fail to reject the null hypothesis at 5% level of significance.")
    print("Conclusion: the given data fits Poisson distribution with parameter ",lamda)
else:
    print("Since p-value<0.05,we reject the null hypothesis at 5% level of significance.")
    print("Conclusion: the given data is not a good fit to Poisson distribution with parameter ",lamda)
#OUTPUT