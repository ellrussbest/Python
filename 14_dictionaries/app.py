# stores key - value pairs

customer = {
    "name": "Michael",
    "age": 30,
    "is_verfied": True,
}

"""
get(key)
get(key, "default value")
"""

"""
program that asks phone number
"""

digit = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

phone_number = input("Phone: ")

if phone_number.isnumeric():
    output = ""
    for number in phone_number:
        output += digit[number] + " "
    print(output)
else:
    print("What you entered is not a number")