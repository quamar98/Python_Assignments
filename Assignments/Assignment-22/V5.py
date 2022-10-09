def sumNCubesNatural(n):
    if n == 0:
        return 0 
    return (n*n*n)+sumNCubesNatural(n-1)
print(sumNCubesNatural(int(input("Enter a number : "))))
