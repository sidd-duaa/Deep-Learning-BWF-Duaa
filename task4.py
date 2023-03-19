# 3-1. Names
names = ['madiha', 'kinza', 'fatima', 'hiba', 'duaa']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

# 3-2. Greetings
print("Hi " + names[1].title() + "!")
print("Hi " + names[2] + "!")

# 3-3. Your Own List
cars = ["Toyota", "BMW", "Audi", "Kia", "Mercedes"]
print("I would like to own a " + cars[4] + ".")

# 3-4. Guest List
diners = ["kinza", "madiha", "hiba"]
print("Hi " + diners[0].title() + "! I would like to have you on dinner tonight.")
print("Hi " + diners[1].title() + "! I would like to have you on dinner tonight.")
print("Hi " + diners[2].title() + "! I would like to have you on dinner tonight.")

# 3-5. Changing Guest List
diners[1] = "fatima"
print("Hi " + diners[0].title() + "! I would like to have you on dinner tonight.")
print("Hi " + diners[1].title() + "! I would like to have you on dinner tonight.")
print("Hi " + diners[2].title() + "! I would like to have you on dinner tonight.")

# 3-6. More Guests
diners.insert(0, "eisha")
diners.insert(2, "rumsha")
diners.append("rabika")
print(diners)
print("Hi " + diners[0].title() + "! I would like to have you on dinner tonight.")
print("Hi " + diners[1].title() + "! I would like to have you on dinner tonight.")
print("Hi " + diners[2].title() + "! I would like to have you on dinner tonight.")
print("Hi " + diners[3].title() + "! I would like to have you on dinner tonight.")
print("Hi " + diners[4].title() + "! I would like to have you on dinner tonight.")
print("Hi " + diners[5].title() + "! I would like to have you on dinner tonight.")

# 3-7. Shrinking Guest List
print("I can only invite two people for dinner, apologies!")
removed = diners.pop()
print ("Sorry I couldn't invite you tonight, " + removed.title())
removed = diners.pop()
print ("Sorry I couldn't invite you tonight, " + removed.title())
removed = diners.pop()
print ("Sorry I couldn't invite you tonight, " + removed.title())
removed = diners.pop()
print ("Sorry I couldn't invite you tonight, " + removed.title())
print(diners)
print("You're still invited, " + diners[0].title())
invited = []
invited.append(diners[0])
del diners[0]
print("You're still invited, " + diners[0].title())
invited.append(diners[0])
del diners[0]
print(diners)
print(invited)

# 3-8. Seeing the world
locations = ["turkey", "germany", "maldives", "france", "italy"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations).reverse())
print(locations)
print(locations.reverse())
print(locations)
print(locations.reverse())
print(locations)
locations.sort()
print(locations)
locations.reverse()
print(locations)

# 3-9. Dinner Guests
print(len(invited))

# 3-10. Every Function
mountains = ["mount everest", "k2", "nanga parbat"]
del mountains[0]
mountains.pop(0)
mountains.remove("nanga parbat")
mountains.append("tirich mir")
mountains.append("nanga parbat")
mountains.insert(2, "rakaposhi")
print(mountains)
print(sorted(mountains))
mountains.reverse()
print(mountains)
mountains.sort()
print(mountains)
print(len(mountains))

# 3-11. Intentional Error
# print(mountains[3])

# 4-1. Pizzas
pizzas = ["Chicago", "California", "Greek"]
for pizza in pizzas:
    print("I like " + pizza.title() + " Pizza")
print("I like Chicago, California and Greek Pizza.\nI really love Pizza")

# 4-2. Animals
animals = ["cat", "dog", "cow"]
for animal in animals:
    print("A " + animal.title() + " would make a great pet")
print("Any of these animals would make a great pet")

# 4-3. Counting to Twenty
for num in range(1,21):
    print(num)

# 4-4. One Million
# for num in range(1,1000000):
#     print(num)

# 4-5. Summing a Million
million = []
for num in range(1,1000001):
    million.append(num)
print(min(million))
print(max(million))
print(sum(million))

# 4-6. Odd Numbers
for num in range(1,21,2):
    print(num)

# 4-7. Threes
for num in range(3,31,3):
    print(num)

# 4-8. Cubes
cubes = []
for i in range(1,11):
    cubes.append(i**3)
for cube in cubes:
    print(cube)

# 4-9. Cube Comprehension
cubes = [num**3 for num in range(1,11)]
print(cubes)

# 4-10. Slices
states = ["texas", "california", "florida", "ohio", "georgia"]
favs = states[:3]
for fav in favs:
    print("The best state is " + fav.title())

middle = states[1:4]
print("The three items from the middle of the list are: " + str(middle))

print("The last three items in the list are: ")
print(states[-3:])

# 4-11. My Pizzas. Your Pizzas
friend_pizzas = pizzas[:]
pizzas.append("vegie")
friend_pizzas.append("pepperoni")
print("My favourite pizzas are: ")
for pizza in pizzas:
    print(pizza.title())
print("My friend's favourite pizzas are: ")
for friendpizza in friend_pizzas:
    print(friendpizza.title())

# 4-13. Buffet
foods = ("Burgers", "Apple Pie", "French Fries", "Hot Dogs", "Pizza")
for food in foods:
    print("The restaurant offers " + str(food))

# foods[0] = "Fried Chicken"

foods = ("Fried Chicken", "Grilled Cheese", "Burgers", "Pizza", "Hot Dogs")
for food in foods:
    print(food)