print("Enter a natural number with open and close [] :") 
x = eval(input())

l = []

for i in x:
    if i%2!=0:
        l.append(i)

print(l)
