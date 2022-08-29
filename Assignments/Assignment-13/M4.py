mylist = ["Java","noSQL","C","Flutter","JavaScript","Python"]

# type one 
'''mylist[1] = "SQL"
mylist[3] = "Reactnative"
print(mylist)'''

#type Two
for i in range(0,len(mylist)):
    if mylist[i] == "noSQL":
        mylist[i] = "SQL"

    if mylist[i] == "Flutter":
        mylist[i] = "Reactnative"

print(mylist)
