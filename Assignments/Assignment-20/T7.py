def fun(n):
    def i(a):
        return a+a
    return i(n)   
print(fun(30))
