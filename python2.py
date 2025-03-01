number1=int(input(“Enter 1st number”))
number2=int(input(“Enter 2nd number”))
number3=int(input(“Enter 3rd number”))
large=int()
if number2>number1:
large=number2
if large<number3:
large=number3
if number1>large:
large=number1
print(“Large number is”, large)
