"""
int()
float()
bool()
type()

above three functions used during conversions

calculate the birth year
"""
birth_year = input('Birth year: ')
age = 2019 - int(birth_year)
print(age)

"""
ask a user of their weight in pounds convert it to
kilograms and print on the terminal
1 pound = 0.45359237 kgs
"""

weight = input('How much do you weigh in pounds? ')
print(float(weight)*0.45359237)
