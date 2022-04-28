# vaccinePortal.py
# Exam number:

# part (iv)
repeat = ""
while repeat != "END":
    s_name = input("Enter your surname: ")
    f_name = input("Enter your first name: ")
    print("Hello",f_name, s_name)
    # part (i)
    age = input("Enter your age: ")
    # part (iii)
    eircode = input("Enter your Eircode: ")
    print("Hello",f_name, s_name,"you are",age,"years old, and your Eircode is",eircode)
    # part (ii)
    age = int(age)
    if age < 50:
        print(f_name,", you will receive the MRNA Vaccine")
    else:
        print(f_name,", you will receive the ADENO Vaccine")
    # part iii
    num = eircode[-1]
    num = int(num)
    # If num even -> Eastwood
    if num % 2 == 0:
        print("Eastwood")
    # If num odd -> Northfield
    else:
        print("Northwood")

    repeat = input("Type END or just press ENTER to exit: ")
    repeat.upper()



