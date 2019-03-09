def call(a,b):
	try:
		operation = input("Enter the operation: like add, sub, multi, div: ")
	except NameError:
		print("Invalid input.")
	else:
		calculate(a,b,operation)

def calculate(a,b,operation):
		if operation == add:
			print(add(a,b))
		elif operation == sub:
			print(sub(a,b))
		elif operation == multi:
			print(multi(a,b))
		elif operation == div:
			print(div(a,b))
		else:
			print("Invalid input")
	
def add(a,b):
	return a + b

def sub(a,b):
	return a - b

def multi(a,b):
	return a * b
	
def div(a,b):
	try:
		return a / b
	except:
		print("The divisable by zero is not accepted.")

def main():
	try:
		a = int(input("Enter the value of a: "))
		b = int(input("Enter the value of b: "))
	except NameError:
		print("Enter the integer value.")
	else:
		call(a,b)

	# 	operation = input("Enter the operation: like add, sub, multi, div: ")

	# calculate(a,b,operation)

	# print(add(a,b))
	# print(sub(a,b))
	# print(multi(a,b))
	# print(div(a,b))
	
main()

