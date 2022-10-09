def nRNaturalEven(n):
    if n > 0:
        if n%2==0:
            print(n)
        nRNaturalEven(n-1)
nRNaturalEven(int(input("Enter a number : "))*2)
