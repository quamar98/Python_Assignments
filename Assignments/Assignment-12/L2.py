n = int(input("Enter a number : "))
temp = 0;

for i in range(2,n):
    if n%i==0:
        temp += 1
if temp == 0:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
    
