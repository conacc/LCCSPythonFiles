# question16(c)ExamPractice.py
# Examination Number:

squared_numbers =[]
num=0
for i in range(20):
    num+=1
    num2=num*num
    squared_numbers.append(num2)
print(squared_numbers)
display=int(input('What squared number will I display(1-20)?'))
print(squared_numbers[display-1])
