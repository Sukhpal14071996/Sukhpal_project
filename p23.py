# Program 23: WAP in python to perform various statistical measures using pandas.

#CODE
import pandas as pd
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'age': [42, 52, 36, 24, 73],
'TestScore': [4, 24, 31, 2, 3]}
df = pd.DataFrame(data, columns = ['name', 'age', 'TestScore'])
df.to_clipboard()
print(df)
print("Mean age= ",df['age'].mean())
print("Statistics of score: \n",df['TestScore'].describe())
print("Count of records: ",df['name'].count())
print("Max score: ",df['TestScore'].max())
print("Min score: ",df['TestScore'].min())
print("Median score: ",df['TestScore'].median())
print("Variance of score: ",df['TestScore'].var())
print("Std Deviation of score: ",df['TestScore'].std())
print("Skewness= ",df['TestScore'].skew())
print("Kurtosis= ",df['TestScore'].kurt())
print(df.corr())
#OUTPUT