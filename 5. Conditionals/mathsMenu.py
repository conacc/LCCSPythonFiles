# mathsMenu.py
# @coneill 16/12/2021
# Menu of maths options
num1 = input('Enter your first number: ')
num1 = int(num1)
num2 = input('Enter your second number: ')
num2 = int(num2)

print('*'*20)
print('0 for Addition,\n1 for Subtraction,\n2 for Multiplication')
print('*'*20)
choice = input('Enter 0, 1 or 2:')
choice = int(choice)
if choice == 0:
    answer = num1+num2
    print(num1,'+',num2,'=',answer)

elif choice == 1:
    answer = num1-num2
    print(num1,'-',num2,'=',answer)
    
elif choice == 2:
    answer = num1*num2
    print(num1,'x',num2,'=',answer)