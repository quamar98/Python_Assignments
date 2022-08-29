n1 = int(input("Enter a first number : "))
n2 = int(input("Enter a second number : "))
n3 = int(input("Enter a third number : "))

if n1>n2 and n1>n3:
    print("first number is greater then second and third number")
elif n2>n1 and n2>n3:
    print("second number is greater then first and third number")
elif n3>n1 and n3>n2:
    print("third number is greater then first and second number")
else:
    print("first,second and third numbers are same")
