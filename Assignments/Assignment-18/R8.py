li1 = ["name","age","gender"]
li2 = ["Quamar",26,"Male"]
li3 = {}

for key in li1:
    for value in li2:
        li3[key] = value
        li2.remove(value)
        break
print(li3)
