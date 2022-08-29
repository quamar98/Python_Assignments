age = int(input("Enter you are age here : "))

match age:
    case age if age<10:
        print("Kid")
    case age if age<20:
        print("Teen")
    case age if age<40:
        print("Young")
    case age if age<60:
        print("Experienced")
    case age if age>= 60:
        print("Senior Citizen")
