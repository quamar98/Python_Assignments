n  = int(input("Enter a number : "))
temp = 0

for i in range(2,n):
    for j in range(2,i-1):
        if i%j==0:
            temp += 1
    if temp==0:
        print(i)
    else:
        temp = 0
