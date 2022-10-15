# # you should take a look at magic methods

# class Point:

#     #constructor
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


#     def move(self):
#         print("move")
    

#     def draw(self):
#         print("draw")

#     def printPoint(self):
#         print(f"({self.x}, {self.y})")


# point1 = Point(0, 1)
# point1.draw()
# point1.move()
# point1.printPoint()


# class Person:
#     def __init__(self, name) -> None:
#         self.name = name

    
#     def talk(self):
#         print(f"Hi I am {self.name}")

# russell = Person("Russell")
# russell.talk()

class employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = self.firstname + "." + self.lastname + "@russell.com"
    
    def giveRaise(self, salary):
        self.salary = salary

class developer(employee):
    def __init__(self, firstname, lastname, salary, programming_language):
        super().__init__(firstname, lastname, salary)
        self.programming_languages = programming_language

    def addLanguages(self, lang):
        self.programming_languages.append(lang)

employee1 = employee("job", "smith", 80000);
print(employee1.salary)

employee1.giveRaise(10000)

print(employee1.salary)

dev1 = developer("joe", "montana", 10000, ["python", "c"])
print(dev1.salary)

dev1.giveRaise(125000)

print(dev1.salary)
dev1.addLanguages("java")
print(dev1.programming_languages)