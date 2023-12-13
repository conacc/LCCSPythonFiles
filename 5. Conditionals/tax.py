# tax.py
# @coneill 13/12/2023
pay = input("Enter your income: ")
pay = int(pay)

if pay < 15000:
    print("You pay no tax")
elif pay < 35000:
    tax = (pay - 15000)*0.2
    print("Your tax to pay: ", tax)
elif pay >= 35000:
    tax = (pay - 15000)*0.2 + (pay - 35000)*0.4
else:
    print("That is not a valid entry")