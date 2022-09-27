# go to search engine and search for python 3 module index

"""
random.randint(10, 20) - returns random values between the specified range
random.choice(list) - randomly pics one value from a list
"""
import random
import math

for i in range(3):
    x = math.ceil(random.random() * 10)
    print(x)


print("\n\n")

class Dice:
    def __init__(self):
        self.x = 1
        self.y = 1


    def roll(self):
        self.x = random.randint(1, 6)
        self.y = random.randint(1, 6)
        return (self.x, self.y)

dice = Dice()
print(dice.roll())