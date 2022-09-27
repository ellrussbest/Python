"""
>
<
<=
>=
!=
==
"""
temperature = 45

if temperature > 30:
    print("it's a hot day")
elif temperature < 10:
    print("it's a cold day")
else:
    print("it's neither hot or cold")


"""
if name is less than 3 characters long
    name must be at least 3 characters
otherwise if it's more than 50 characters long
    name can e a maxmum of 50 characters
otherwise name looks good!
"""

name = input("Enter your name young'un...")

if len(name) < 3:
    print('name must be at least 3 characters')
elif len(name) > 50:
    print('name can be a maximum of 50 characters')
else:
    print('name looks good!')

 