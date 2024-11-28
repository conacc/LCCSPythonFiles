# Question 16(a)
# Name and School

cardNum=7200828282828210
# part (i) and part (iii)
cardNum = input("Welcome to CardCheck. Enter your card number:")

for num in range(2):
    cardLength = len(cardNum)
    if cardLength == 16:
        blocked = False # part (vi) - Boolean used here
    else:
        cardNum = input("Please re-enter your card number:")
        blocked = True

if blocked == False:
    print(cardNum)
    #part (ii)
    cardNum = str(cardNum)
    if cardNum[0] == "7":
        print("This is a ZincCard")
    elif cardNum[0] == "8":
        print("This is a WinCard")
    else:
        print("This is neither")
    # part (v)
    expiry = input("Enter the card expiry date e.g. 11/26 should be entered as 1126:")
    firstTwo = int(cardNum[0]+cardNum[1])
    cvv = (int(expiry[0]+expiry[1]+expiry[2]+expiry[3])*firstTwo)-int(cardNum[9])
    print("CVV number:",cvv)
    
    # part (vii)
    print("Card number: "+cardNum[:4]+"-"+cardNum[4:8]+"-"+cardNum[8:12]+"-"+cardNum[12:16]+" and it is valid")
    
elif blocked == True:
    print("You are blocked")