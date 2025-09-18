print("Creating an empty tuple..."); 
my_tuple = (); 
print("An empty tuple, my_tuple is created successfully."); 
if not my_tuple: 
    print("The tuple, my_tuple, contains no any item."); 
print("Inserting some items to the tuple..."); 
my_tuple = ("me", "my friend", "my brother", "my sister"); 
print("\nPrinting the tuple..."); 
print(my_tuple); 
print("\nNow printing each item in the tuple..."); 
for item_in_tuple in my_tuple: 
    print(item_in_tuple);
