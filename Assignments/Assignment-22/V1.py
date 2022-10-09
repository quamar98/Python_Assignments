def sumNNaturalNumber(n):
    if n == 0:
        return 0
    return n + sumNNaturalNumber(n-1)

print(sumNNaturalNumber(int(input("Enter a number : "))))
