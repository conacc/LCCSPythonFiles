# Question 16(a)
# Name: Ada Lovelace

pin = "1579"
loggedIn = False # part (iii)
failedAttempts = 0 # part (vi)
# The input function asks user for PIN and
# saves it as the variable userTry - part (i)
while loggedIn == False and failedAttempts<3:   # part (v)
    userTry = input("Enter PIN:")

    if userTry == pin:
        print("Welcome")
        loggedIn = True # part (iv)
    # part (ii)
    else:
        print("Incorrect PIN")
        failedAttempts = failedAttempts + 1
    
if failedAttempts == 3:
    print("You have entered the PIN incorrectly 3 times")
    
    