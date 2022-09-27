is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
elif is_cold:
    print("go fuck yourselves")
else:
    print("Enjoy your day")

"""
price of a house is $1M.
if a buyer has good credit,
    they need to put down 10%
otherwise
    they need to put down 20%
print the down payment
"""

price = 1000000 
has_good_credit = True

if has_good_credit:
    downpayment = price // 10
else:
    downpayment = price // 5

print(downpayment)