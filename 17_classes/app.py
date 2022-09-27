# you should take a look at magic methods

class Point:

    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print("move")
    

    def draw(self):
        print("draw")

    def printPoint(self):
        print(f"({self.x}, {self.y})")


point1 = Point(0, 1)
point1.draw()
point1.move()
point1.printPoint()


class Person:
    def __init__(self, name) -> None:
        self.name = name

    
    def talk(self):
        print(f"Hi I am {self.name}")

russell = Person("Russell")
russell.talk()