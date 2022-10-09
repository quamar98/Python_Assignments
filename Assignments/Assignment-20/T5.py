#type one
def minNumber(a,b,c):
    temp = []
    temp.append(a)
    temp.append(b)
    temp.append(c)
    print(min(temp))
minNumber(3,4,5)

#type two
def minNumber(*n):
    print(min(*n))
minNumber(3,4,5)
