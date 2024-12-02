# Question 16 (b)
# Student name:
import random
ticket = []

user_number = int(input("Please pick a number between 1 and 10: "))
ticket.append(user_number)
user_number = int(input("Please pick a number between 1 and 10: "))
ticket.append(user_number)
user_number = int(input("Please pick a number between 1 and 10: "))
ticket.append(user_number)

print("Your ticket is: ", ticket)
print("The draw will start now, good luck!")
drum = [1,2,3,4,5,6,7,8,9,10]
result = []
def lotto(ticket):
    for times in range (3):
        draw = drum[random.randint(0,len(drum))-1]
        result.append(draw)
    print("The draw was: ", result)
 
lotto(ticket)
