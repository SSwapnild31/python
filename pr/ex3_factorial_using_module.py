import math

try:
	num = int(input("Enter num : "))
except ValueError:
	print("Invalis i/p..!")
	exit()

if num<0 :
	print("num is negative")
elif num==0:
	print("The factorial of 0 is 1")
else :
	res = math.factorial(num)
	print(f"The factorial of {num} is {res}.")
