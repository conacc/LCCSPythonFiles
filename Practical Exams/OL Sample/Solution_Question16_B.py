# question16(b)ExamPractice.py
# Examination Number:

# This function multiplies two numbers 
def multiply(x, y):
    return x*y

# This function divides two numbers
def divide(x, y):
    ans=x/y
    ans=round(x/y,2)
    return ans

def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y
cal=int(input('How many calculations will i do?:'))
# Main Program
import random # To generate random numbers
num=0
for i in range(cal):
    num+=1
    print('Calculation',num)
    print("Select operation.")
    print("1.Multiply")
    print("2.Divide")
    print('3.addition')
    print('4.Subtraction')
# Take input from the user 
    choice = input("Enter choice(1/2/3/4):")

#num1 = random.randint(1,12)
#num2 = random.randint(1,12)
    num1=int(input('Enter first number:'))
    num2=int(input('Enter second number:'))

    if choice == '1':
        print(num1,"*",num2,"=", multiply(num1,num2))
    elif choice == '2':
        print(num1,"/",num2,"=", divide(num1,num2))
    elif choice =='3':
        print(num1,'+',num2,'=',addition(num1,num2))
    elif choice =='4':
        print(num1,'-',num2,'=',subtraction(num1,num2))