# gradeCalc.py
# @coneill 14/12/2021
# Calculate LC grades
mark = input('Enter HL mark: ')
mark = int(mark)
if mark >= 90:
    print('H1')
elif mark >= 80:
    print('H2')
elif mark >= 70:
    print('H3')
elif mark >= 60:
    print('H4')
elif mark >= 50:
    print('H5')
elif mark >= 40:
    print('H6')
elif mark >= 30:
    print('H7')
else:
    print('H8')