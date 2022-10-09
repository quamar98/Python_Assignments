def nNaturalOdd(n):
    if n > 0:
        if n%2!=0:
            print(n)
        nNaturalOdd(n-1)
nNaturalOdd(int(input("Enter a number : "))*2)
