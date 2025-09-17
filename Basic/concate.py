my_list = ["zero", "one", "two", "three", "four"]; 
my_new_list = ["five", "six"]; 
my_list += my_new_list; 
print("List's items after concatenating:"); 
for l in my_list: 
    print(l);
#To delete any element from a list in python 
# Deleting element from list in python example 
my_list = ["zero", "one", "two", "three", "four"]; 
print("Elements of the list, my_list are:"); 
for ml in my_list: 
    print(ml); 
index = input("\nEnter index no:"); 
index = int(index); 
print("Deleting the element present at index number",index); 
del my_list[index]; 
print("\nNow elements of the list, my_list are:"); 
for ml in my_list: 
    print(ml);
