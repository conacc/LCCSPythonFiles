# practicleExamPratcise.py
# Examination Number:
#This calculator can only addand subtract
num1 = 9
num2 = 5

name=input('Please enter your name: ')
print('Hello',name,' Welcome to the addition and subtraction calculator')
num1=int(input('What do you want your first number to be?:'))
num2=int(input('What do you want your second number to be?:'))
choice = input('Do you want me to (a)dd or (s)ubtract?')
choice=choice.lower()
if choice == 'a':
    print (num1,'+',num2,'=',num1 + num2)
elif choice == 's':
    print (num1,'-',num2,'=',num1 - num2)
else:
    while choice!='a' or choice!='s':
        print('Invalid option')
        choice = input('Do you want me to (a)dd or (s)ubtract?')
        choice=choice.lower()
        if choice == 'a':
            print (num1,'+',num2,'=',num1 + num2)
            break
        elif choice == 's':
            print (num1,'-',num2,'=',num1 - num2)
            break