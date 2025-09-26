#1
mylist = ["apple","banana","cherry"]
print(type(mylist))

#2
thislist = ["apple","banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#3
thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist)

#4
thislist = ["apple","banana","cherry"]
for x in thislist:
    print(x)

#5
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)
