def primeOrNot(n):
    temp = 0
    for i in range(2,n-1):
        if n%i==0:
            temp += 1
    if temp == 0:
        print("Prime number")
    else:
        print("Not a Prime number")
primeOrNot(3)
