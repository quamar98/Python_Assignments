def evenNumber(a):
    li = []
    for i in range(1,len(a)):
        if i%2==0:
            li.append(i)
    print(li)
evenNumber([1, 2, 3, 4, 5, 6, 7, 8, 9])
