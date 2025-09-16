Starting_value = 1 
# Taking input from the user 
n = int(input("Enter the number: ")) 
print("Prime numbers between", Starting_value, "and", n, "are:") 
for num in range(Starting_value, n + 1): 
    if num > 1: 
        for i in range(2, int(num/2)+1):
            if (num % i == 0): 
                break;
            else: 
                print(num)
