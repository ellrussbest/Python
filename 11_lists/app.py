# 2-D list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for list in matrix:
    output = ''
    for element in list:
        output += (str(element) + ' ')
    print(output)

print(matrix)

# list operations

"""
append() - adds a new number at the end of the list
insert(index, object) - inserts the new object at the specific position
remove(object) - deletes a specific object in the list
clear() - deletes everything from the list
pop() - deletes the last object from the list
index(object) - returns the index of the first occurence of an item
in - operator used to check the existence of an object in a list
count(object) - returns the number of objects occuring in a list
sort() - used to sort list
reverse() - reverses the list
copy() - we can get a copy of our list
"""
# write a program to remove duplicates in a list

numbers = [1, 2, 3, 3, 1, 2, 5]
newlist = []

for number in numbers:
    if number in newlist:
        continue
    else:
        newlist.append(number)

print(newlist)