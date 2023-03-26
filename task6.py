# Dictionaries

# 6-1. Person
person = {'fname':'hiba', 'lname':'asif', 'age':21, 'city':'karachi'}

# 6-2. Favourite Numbers
favnum = {'kinza':21, 'hiba':18, 'duaa':3, 'madiha':12}
for key,value in favnum.items():
    print("Key: "+ key)
    print("Value: "+ str(value) )

favnum['fatima'] = 32
print(favnum)

del favnum['kinza']
print(favnum)

# 6-4. Glossary
programming = {'variables':'containers to store values',
               'conditionals':'if then else',
               'list':'containers to store multiple values',
               'datatypes':'type of data'}
for words,meanings in programming.items():
    print(words + " : " + meanings)

# 6-5. Rivers
rivers = {'amazon':'south america',
          'nile':'egypt',
          'congo':'africa',
          'yangtze':'china',
          'mississippi':'usa'}
for river,country in rivers.items():
    print("The "+river+" river runs through "+country)
for river,country in rivers.items():
    print(river)
for river,country in rivers.items():
    print(country)

# 6-7 People
person1 = {'fname':'hiba', 'lname':'asif', 'age':21, 'city':'karachi'}
person2 = {'fname':'kinza', 'lname':'akhtar', 'age':20, 'city':'karachi'}
person3 = {'fname':'madiha', 'lname':'aftab', 'age':22, 'city':'karachi'}
people = [person1,person2,person3]
for person in people:
    print(person)

# 6-9. Favourite Places
favplaces = {'hiba':['maldives','machu picchu'],'kinza':['greece'],'madiha':['paris, vanice']}
for person,places in favplaces.items():
    print(person)
    for place in places:
        print(place)

    
# 6-11. Cities
cities = {'karachi':['pakistan', 14.91, 'city of lights'],
          'paris':['france',2.161,'has eiffel tower'],
          'istanbul':['turkey',15.46,'major city']}
for city,citiesinfo in cities.items():
    print(city.upper())
    for cityinfo in citiesinfo:
        print(cityinfo)

