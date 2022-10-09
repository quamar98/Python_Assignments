def nNatural(n):
    if n > 0:
        print(n)
        nNatural(n-1)
nNatural(int(input("Enter a number : ")))
