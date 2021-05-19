# Question 1 Solution
# Name: C O'Neill
# This calculator can only add and subtract
name = input('Please enter your name: ')
print('Welcome to add/subtract',name)
num1 = input('Please enter first num: ')
num1 = int(num1)
num2 = input('Please enter second num: ')
num2 = int(num2)
choice = 'start'
while choice != 'finish':
    choice = str(input('Do you want to (a)dd or (s)ubtract?: '))
    if choice == 'a' or choice =='A':
        print(num1,'+',num2,'=',num1+num2)
        choice = 'finish'
    elif choice == 's' or choice =='S':
        print(num1,'-',num2,'=',num1-num2)
        choice = 'finish'
    else:
        print('Invalid entry')
    
    
    
    
    