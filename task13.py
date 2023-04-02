import pandas as pd
from pandas import Series, DataFrame

# Series

obj = pd.Series([4,7,-5,3])
# print(obj)
# print(obj.values)
# print(obj.index)

obj2 = pd.Series([4,7,-5,3], index = ['d','b','a','c'])
# print(obj2)
# print(obj2.values)
# print(obj2.index)
# print(obj2['a'])
obj2['d'] = 6
# print(obj2[['c','a','d']])
# print(obj2[obj2>0])
# print(obj2*2)
# print('b' in obj2)


sdata = {'Ohio':35000, 'Texas':71000, 'Oregon':16000}
obj3 = pd.Series(sdata)
# print(obj3)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index = states)
# print(obj4)
# print(pd.isnull(obj4))
# print(obj4.isnull())
# print(pd.notnull(obj4))
# print(obj4.notnull())

# print(obj3 + obj4)

obj4.name = 'population'
obj4.index.name = 'state'

# print(obj4)

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
# print(obj)

# DataFrame

data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year':[2000, 2001, 2002, 2001, 2002, 2003],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
# frame = pd.DataFrame(data)
frame = pd.DataFrame(data, columns = ['year', 'state', 'pop'])
# print(frame)
# print(frame.head())
frame2 = pd.DataFrame(data, columns = ['debt', 'year', 'state', 'pop'], index = ['one', 'two', 'three', 'four', 'five', 'six'])
# print(frame2.columns)
# print(frame2['state'])
# print(frame2.year)
# print(frame2.loc['three'])
frame2['debt'] = 16.5
# print(frame2)

val = pd.Series([-1.2, -1.5, -1.7], index = ['two', 'four', 'five'])
frame2['debt'] = val
# print(frame2)

frame2['eastern'] = frame2.state == 'Ohio'
# print(frame2)
del frame2['eastern']
# print(frame2.columns)

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
# print(frame3.T)
# frame3 = pd.DataFrame(pop,index=[2001,2002,2003])
# print(frame3)

pdata = {'Ohio': frame3['Ohio'][:-1],
          'Nevada':frame3['Nevada'][:2]}
print(pd.DataFrame(pdata))