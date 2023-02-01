# Question 16 (a)
# Examination Number:

firstName = input("What is your first name? ")

print("Hello", firstName)
print("Please select from the list of items.\n")
# \n creates a new line

print("\tItems Available")# \t creates a tab
print("1 = Book")

shoppingItem = int(input("\nEnter the number of the item you would like: "))

if shoppingItem == 1:
    print("You bought a book")