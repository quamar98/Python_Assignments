print("Enter a list use with open and close [] ;")
x = [1,2,3,'hello',3.4,'my',5.5,4.8]
y = []
for i in x:
    if type(i)==int:
        y.append(i)

print(y)
