import pandas as pd

# Read csv file
df = pd.read_csv('pokemon_csv.csv')
'''print(df)
print(df.head(3)) #above three rows
print(df.tail(3)) #last three rows'''

# Read excel file
'''df_xlsx = pd.read_excel('pokemon_excel.xlsx')
print(df_xlsx.head(2))'''

# Read txt file
# df_txt = pd.read_csv('pokemon_txt.txt', delimiter='\t')
# print(df_txt.head(2))

# Reading headers
# print(df.columns)

# Reading columns
# print(df['HP'])
# print(df['HP'][0:5]) #top five values of column
# print(df.Name)
# print(df[['Name','HP', 'Type 1']])

# Reading rows
# print(df.iloc[1])
# print(df.iloc[0:4])

# Reading specific location
# print(df.iloc[2,1])

data = '{"employee_name": "James", "email": "james@gmail.com", "job_profile": [{"title1":"Team Lead", "title2": "Sr. Developer"}]}'
df_json = pd.read_json(data)
print(df_json)