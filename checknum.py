x = input("Enter a number of x: ")
y = input("Enter a number of y: ")
z = input("Enter a number of z: ")

if x > y and x > z:
		print(f"{x} is greater than {y} and {z}")
elif y > x and y > z:
		print(f"{y} is greater than {x} and {z}")
elif z > x and z > y: 
	print(f"{z} is greather than {x} and {y}")
elif x == y and x == z and y == x and y == z and z == x and z ==y:
	print("all number are equal")

print("thanks!")

#this program there is a error same value gives greater
# need to check