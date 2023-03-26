# File Handling

'''file = open("bwt.txt", 'r')
# print(file.read(4))
# content = file.read()
# print(content)
for lines in file:
    print(lines)
print(file.readline(),end='')

file.close()'''

'''file = open('bwt.txt','w')
file.write("Task 8 contains classes")'''

'''file = open('bwt.txt', 'a')
file.write("Tasks accomplished")'''

# Exception Handling

try:
    open('this.txt')
except Exception as e:
    pass
finally:
    print("This will be printed in every case")
    # print(e)