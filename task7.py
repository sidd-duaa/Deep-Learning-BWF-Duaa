# Functions

# 8-1. Message
def dispmsg():
    print('Learning functions')

dispmsg()

# 8-2. Favourite Book
def favbook(title):
    print("I really like " + title)

favbook("Jane Eyre")

# 8-3. T-Shirt
def makeshirt(size,text):
    return ("The shirt is of size " + str(size) + " printing " + text + " on it")

print(makeshirt(18,'"good things take time"'))
print(makeshirt(size = 18, text = '"good things take time"'))

# 8-4. 
def makeshirt(text, size='large'):
    return ("The shirt is of size " + str(size) + " printing " + text + " on it")

print(makeshirt('"good things take time"'))
print(makeshirt(text = '"good things take time"'))

# 8-7. Album
def make_album(artist, title):
    album = {artist:title}
    return album
print(make_album('niravana','nevermind'))

# 8-12. Sandwiches
def sandwich(*toppings):
    for topping in toppings:
        print(topping)

sandwich('mustard', 'pepper', 'mayonnaise')

# Docsting
def average(num1, num2):
    '''This is the function which will print average of two numbers'''
    avg = (num1+num2)/2
    return avg

print(average.__doc__)
print(average(3,5))

