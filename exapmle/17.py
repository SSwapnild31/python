#1
thislist = [100,50,65,82,23]
thislist.sort()
print(thislist)

#2
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort(reverse = True)
print(thislist)

#3
thislist = [100,50,65,82,23]
thislist.sort(reverse = True)
print(thislist)

#4
def myfunc(n):
    return abs(n-50)
thislist = [100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)



