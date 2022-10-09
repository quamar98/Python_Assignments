def squaresNNaturalNumber(n):
    if n == 0:
        return 0
    return (n*n) + squaresNNaturalNumber(n-1)
print(squaresNNaturalNumber(int(input("Enter a number : "))))
