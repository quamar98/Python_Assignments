n  = int(input("Enter a number : "))
s = 0

for i in range(1,n*2):
    if i%2!=0:
        s = s + i
        print(s)
