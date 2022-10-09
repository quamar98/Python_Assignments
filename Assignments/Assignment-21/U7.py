def nNaturalsquares(n):
    if n > 0:
        nNaturalsquares(n-1)
        print(n*n)
nNaturalsquares(int(input("Enter a number : ")))
