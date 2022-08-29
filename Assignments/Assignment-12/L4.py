n = int(input("Enter a start number : "))
m = int(input("Enter a end number : ")) 
temp = 0

for i in range(n,m):
    for j in range(2,i-1):
        if i%j==0:
            temp += 1
    if temp==0:
        print(i)
    else:
        temp = 0
