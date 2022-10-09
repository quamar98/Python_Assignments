def nNaturalOdd(n):
    
    if n > 0:
        nNaturalOdd(n-1)
        if n%2!=0:
            print(n)
nNaturalOdd(int(input("Enter a number : "))*2)
