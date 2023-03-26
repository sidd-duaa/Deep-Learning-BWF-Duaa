# Enumerate Function
usernames = ['eric','james','admin']
for index,users in enumerate(usernames):
    if users == 'admin':
        print("Hey admin, Would you like a status report")
    else:
        print("Hi " + users + " Thanks for logging again")

# Conditionals

# 5-1. Conditional Tests
food = 'burger'
print("Is food == 'burger'? I predict True.")
print(food == 'burger')
print("\nIs food == 'pizza'? I predict False.")
print(food == 'pizza')

# 5-2. More Conditional Tests
car = 'audi'
print(car != 'audi')

car = "Audi"
print(car.lower() == 'audi')

num = 16
print(num >= 12)
print(num <= 12)

print(num >= 14 and num <= 50)
print(num >= 20 or num <= 50)

foods = ['burger', 'pizza', 'fries']
print('hot dog' in foods)
print('hot dog' not in foods)

# 5-3. Alien Colors 1
alien_color = 'green'
if (alien_color == 'green'):
    print("You just earned 5 points")

# 5-4. Alien Colors 2
alien_color = 'red'
if (alien_color == 'green'):
    print("You just earned 5 points")
else:
    print("You just earned 10 points")

# 5-5. Alien Colors 3
alien_color = 'yellow'
if (alien_color == 'green'):
    print("You just earned 5 points")
elif (alien_color == 'yellow'):
    print("You just earned 10 points")
else:
    print("You just earned 15 points")

# 5-6. Stages of Life
age = 21
if (age < 2):
    print('Person is a baby')
elif (age >= 2 and age <= 4):
    print('Person is a toddler')
elif (age >= 4 and age <= 13):
    print('Person is a kid')
elif (age >= 13 and age <= 20):
    print('Person is a teenager')
elif (age >= 20 and age <= 65):
    print('Person is an adult')
elif (age >= 65):
    print('Person is elderly')

# 5-7. Favourite Fruit
fav_fruits = ['Strawberry', 'Apple', 'Oranges']
if 'Strawberry' in fav_fruits:
    print("I really like Strawberry")
if 'Banana' in fav_fruits:
    print("I really like banana")
if 'Apple' in fav_fruits:
    print("I really like apple")
if 'Oranges' in fav_fruits:
    print("I really like oranges")
if 'Grapes' in fav_fruits:
    print("I really like grapes")

# 5-8. Hello Admin
usernames = ['eric','jen','admin','james','david']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hi " + username + ", Thanks for logging in again")

# User Inputs

'''# 7-1. Rental Car
car = input("What kind of rental car do you want?")
print("Let me see if I can find you a "+ car)

# 7-2. Restaurant Seating
group = int(input("How many people are in your dinner group?"))
if group >= 8:
    print("You'll have to wait for the table")
else:
    print("Your table is ready")'''

# Sets

s1 = set([1,2,3,4])
s2 = set([1,2,5])
s1.add(1)
s1.remove(4)
print(s1)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.isdisjoint(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

l1 = [1,2,3,1,6,3]
s3 = set(l1)
print(s3)

# Timing your code
import time
initial = time.time()
print(initial)