def nNaturalEven(n):
    if n > 0:
        nNaturalEven(n-1)
        if n%2==0:
            print(n)
nNaturalEven(int(input("Enter a number : "))*2)
