s1 = input("Enter you are first string : ")
s2 = input("Enter you are second string : ")

match s1:
    case s1 if s1<s2:
        print(s1,s2)
    case s1 if s1>s2:
        print(s2,s1)
