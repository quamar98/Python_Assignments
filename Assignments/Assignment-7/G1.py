n = int(input("Enter a month value in numeric format : "))

match n:
    case 1:
        print("No.of days is : 31 days")
    case 2:
        print("No.of days is : 28/29 days")
    case 3:
        print("No.of days is : 31 days")
    case 4:
        print("No.of days is : 30 days")
    case 5:
        print("No.of days is : 31 days")
    case 6:
        print("No.of days is : 30 days")
    case 7:
        print("No.of days is : 31 days")
    case 8:
        print("No.of days is : 31 days")
    case 9:
        print("No.of days is : 30 days")
    case 10:
        print("No.of days is : 31 days")
    case 11:
        print("No.of days is : 30 days")
    case 12:
        print("No.of days is : 31 days")
    case _:
        print("Your enter a wrong month number")
