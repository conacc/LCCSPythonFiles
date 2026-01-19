# fizzBuzzToTestV1.py
# @coneill 19/01/2026
def FB(x):
    if x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x
        
num = int(input("Enter a number:"))
answer = FB(num)
print(answer)