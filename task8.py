# Classes

class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Configuration is ', self.cpu, self.ram)

comp1 = Computer('i5', 16)
comp2 = Computer('i3', 8)

comp1.config()
comp2.config()

# Inheritance

class Teacher:
    def course1(self):
        print('Database')
    def course2(self):
        print('Automata')

class Student(Teacher):
    def course3(self):
        print('Soft. Eng.')
    def course4(self):
        print('Data Structures')

teach1 = Teacher()

std1 = Student()
std2 = Student()

std1.course1()
std2.course2()
std2.course3()
