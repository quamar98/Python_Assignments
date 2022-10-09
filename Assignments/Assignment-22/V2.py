def OddSum(n):
    if n == 1 :
        return 1
    return ((2*n)-1) + OddSum(n-1)
print(OddSum(int(input("Enter a number : "))))
