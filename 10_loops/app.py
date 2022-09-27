i = 1

while i <= 5:
    print(i)
    i = i + 1
print('Done')

"""
guessing game

while loops can have else part e.g

while
    body
else
    body
"""

count = 1
correct_guess = '9'

while True:
    guess = input("Guess: ")
    if count >= 3:
        print('Sorry you failed!')
        break
    if guess == correct_guess:
        print('You guessed right!!!')
        break
    count = count + 1

while True:
    store = input('>').upper()

    if store == 'HELP':
        print("""
                start - to start the car
                stop - to stop the car
                quit - to exit
        """)
    elif store == 'QUIT':
        break
    elif store == 'START':
        print('Car started... Ready to go!')
    elif store == 'STOP':
        print('Car stopped')
    else:
        print("I don't understand that")

"""
for loop
"""
for item in 'Python':
    print(item)

for item in ['mosh', 'john', 'sarah']:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 10, 2):
    print(item)



"""
write a program to calculate the total cost of 
items in a shopping cart

"""
total = 0

for item in [1, 2, 3]:
    total += item

print(total)