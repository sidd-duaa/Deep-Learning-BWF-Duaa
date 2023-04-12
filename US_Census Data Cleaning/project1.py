import pandas as pd
import glob
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

# Loading Datasets
states = glob.glob('*.csv')
# print(states)

# Reading CSVs
dataset = []
for state in states:
    dataset.append(pd.read_csv(state))

# Concatenating files
us_census = pd.concat(dataset)

# Name and Information
print(us_census.head())
print(us_census.columns)
print(us_census['Income'].dtype)

# Changing dtypes
us_census['Income']=pd.to_numeric(us_census['Income'].replace('\$','',regex=True))
us_census['Pacific']=pd.to_numeric(us_census['Pacific'].str.replace('%',''))
us_census['Asian']=pd.to_numeric(us_census['Asian'].str.replace('%',''))
us_census['Hispanic']=pd.to_numeric(us_census['Hispanic'].str.replace('%',''))
us_census['White']=pd.to_numeric(us_census['White'].str.replace('%',''))
us_census['Black']=pd.to_numeric(us_census['Black'].str.replace('%',''))
us_census['Native']=pd.to_numeric(us_census['Native'].str.replace('%',''))

# Splitting Men and Women
us_census[['Men', 'Women']] = us_census['GenderPop'].str.split('_', expand = True)

# Converting to numerical dtypes
us_census['Men'] = pd.to_numeric(us_census['Men'].str.replace('[,M]', '', regex = True))
us_census['Women'] = pd.to_numeric(us_census['Women'].str.replace('[,F]', '', regex = True))

print(us_census['Women'])

# Filling NaN Values
us_census['Women'] = us_census['Women'].fillna(us_census['TotalPop'] - us_census['Men'])

print(us_census['Women'])

# Dropping Duplicates
us_census = us_census.drop_duplicates()
# print(dataset)

# Scatter Plot
Proportion_of_women = us_census['Women']/us_census['TotalPop']
Average_Income = us_census['Income']
plt.scatter(Proportion_of_women, Average_Income)
plt.xlabel('Porportion of Women')
plt.ylabel('Average Income')
plt.show()

print(us_census.columns)

# Filling NaN Values
us_census=us_census.fillna(value={'Asian':0,'Black':0,'White':0,'Pacific':0,'Hispanic':0,'Native':0})

# Histograms
Hispanic = us_census['Hispanic']
plt.hist(Hispanic)
plt.title('Hispanics')
plt.show()

White = us_census['White']
plt.hist(White)
plt.title('Whites')
plt.show()

Black = us_census['Black']
plt.hist(Black)
plt.title('Black')
plt.show()

Native = us_census['Native']
plt.hist(Native)
plt.title('Native')
plt.show()

Asian = us_census['Asian']
plt.hist(Asian)
plt.title('Asian')
plt.show()

Pacific = us_census['Pacific']
plt.hist(Pacific)
plt.title('Pacific')
plt.show()