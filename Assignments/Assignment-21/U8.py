def nNaturalcubes(n):
    if n > 0:
        nNaturalcubes(n-1)
        print(n*n*n)
nNaturalcubes(int(input("Enter a number : ")))
