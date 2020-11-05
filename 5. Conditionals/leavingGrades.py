# leavingGrades.py
# @coneill 4/11/2020
# Asks user for % result and shows LC grade
result = input('Please enter % result: ')
result = int(result) # Convert result to integer

if result > 100:
    print('You did not enter a valid % result')

elif result < 0:
    print('You did not enter a valid % result')

elif result >= 90:
    print('H1')

elif result >= 80:
    print('H2')

elif result >= 70:
    print('H3')

elif result >= 60:
    print('H4')

elif result >= 50:
    print('H5')
    
elif result >= 40:
    print('H6')

elif result >= 30:
    print('H7')

else:
    print('H8')
