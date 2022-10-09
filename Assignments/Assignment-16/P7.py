tuple1=(1,2,3,4,5,6)
li = []
for i in tuple1:
    if i == 4 :
        li.append(i)
    elif i == 5:
        li.append(i)
tuple2 = tuple(li)
print(tuple1)
print(tuple2,type(tuple2))
