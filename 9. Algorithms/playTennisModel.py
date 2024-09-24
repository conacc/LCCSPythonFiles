# playTennisModel.py
# @coneill 24/09/2024

# Define Function
def tennis(outlook, humidity, wind):
    if outlook == "overcast":
        return "yes" # output from function
    elif outlook == "sunny":
        if humidity == "high":
            return "no"
        elif humidity == "normal":
            return "yes"
    elif outlook == "rain":
        if wind == "strong":
            return "no"
        elif wind == "weak":
            return "yes"
    else:
        return -1
# Call Function
decision = tennis("suuny","normal","weak")
if decision == -1:
    print("Invalid entry")
else:
    print("Should you play Tennis?",decision)
