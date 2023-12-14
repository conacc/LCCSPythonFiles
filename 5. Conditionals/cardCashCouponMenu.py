# cardCashCouponMenu.py
# @coneill 14/12/2023
payType = input("Would you like to pay using cash, card or coupon?")

if payType == "cash":
    print("Please insert cash")
    
elif payType == "card":
    print("Please insert your card into the machine")

elif payType == "coupon":
    print("Coupons are only accepted at the customer service desk")
    
else:
    print("That is not a valid entry")