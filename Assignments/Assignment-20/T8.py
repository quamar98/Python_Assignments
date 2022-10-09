def strCal(n):
    count1 = 0
    count2 = 0
    count3 = 0
    for i in n:
        if i == i.upper():
            count1 += 1
        else:
            count2 += 1
    print("Number of uppercase is : ",count1)
    print("Number of lowercase is : ",count2)
strCal("QuamAruddiN")
