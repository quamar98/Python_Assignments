tuple1=(100, 200, 300, 400)
v1 = []
v2 = []
v3 = []
v4 = []

for i in tuple1:
    if i == 100:
        v1.append(i)
    elif i == 200:
        v2.append(i)
    elif i == 300:
        v3.append(i)
    else:
        v4.append(i)
print(tuple(v1))
print(tuple(v2))
print(tuple(v3))
print(tuple(v4))
