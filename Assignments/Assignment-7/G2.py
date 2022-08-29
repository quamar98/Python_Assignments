a = eval(input("Enter a first number : "))
b = eval(input("Enter a second number : "))
op = input("Choose your operater + , - , * , / : ")

match op:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case _:
        print("you are enter a invalid operater")
