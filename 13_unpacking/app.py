# this is like destructuring
# we can do unpacking to both lists and tuples

numbers = (1, 2, 3)
x, y, z = numbers

print (f'{x}, {y}, {z}')

list = [1, 'b', True, 300.0]
w, x, y, z = list
print (f'{w}, {x}, {y}, {z}')

print(type(y))