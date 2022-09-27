# def function_name (parameters):
# calling a function: function_name(arguments)
def greet_user():
    print('Hi there!')
    print('Welcome aboard')


greet_user()

def add_two_numbers(a = 0, b = 0):
    return a + b

print(add_two_numbers(3, 4))
print(add_two_numbers())

# keyword arguments: function_name(parameter=argument) e.g.
# get_user(first_name="john")