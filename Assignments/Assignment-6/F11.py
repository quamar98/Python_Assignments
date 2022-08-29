n = int(input("Enter a month value in numeric format : "))

if n == 2:
    print("No. of days: 28/29 days")
elif n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print("No. of days: 31 day")
elif n==4 or n==6 or n==9 or n==11:
    print("No. of days: 30 days")
else:
    print("You enter wrong month number") 
