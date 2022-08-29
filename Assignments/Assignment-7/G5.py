num = int(input("Enter a number : "))

match num:
    case num if num%2==0:
        print("Saurabh Shukla")
    case num if num%2!=0 and num<0:
        print("Prateek Jain")
    case num if num%2!=0:
        print("Aditya Choudhary")
