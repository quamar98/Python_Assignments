def nNatural(n):
    if n > 0:
        nNatural(n-1)
        print(n)
nNatural(int(input("Enter a number : ")))
