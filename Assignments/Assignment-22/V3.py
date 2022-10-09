def sumNEvenNumber(n):
    if n == 0 :
        return 0
    return (2*n) + sumNEvenNumber(n-1)
print(sumNEvenNumber(int(input("Enter a number : "))))
