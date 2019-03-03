
# def iseven(n):
# 	if n%2 == 0:
# 		return True

# 	return False

# def main():

# 	a = int(input("Enter a number: "))
# 	print(iseven(a))

# main()

# def circle_area(r):

# 	pi = 22/7
# 	area = pi*(r**2)
# 	return area

# print(circle_area(12))

# def fact(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		return n*fact(n-1)

# print(fact(5))

#fn that takes in radius and height and gives area of cylinder

# def cylinder(r,h):
# 	pi = 22/7
# 	return 2*pi*r*h + (2*pi*r)**2


# def main():
# 	r = int(input("enter a radius: "))
# 	h = int(input("enter a height: "))
# 	return(cylinder(r,h))

# print(main())

# import math 

# def distance(x1,x2,y1,y2):
# 	result = (x1-x2)**2 + (y2-y1)**2
# 	return math.sqrt(result)

# def main():
# 	x1 = int(input("enter a x1: "))
# 	x2 = int(input("enter a x2: "))
# 	y1 = int(input("enter a y1: "))
# 	y2 = int(input("enter a y2: "))
# 	return distance(x1,x2,y1,y2)

# print(main())

# def fib(n):
# 	if n == 1 or n == 2:
# 		return 1
# 	else:
# 		return fib(n-1) + fib(n - 2)

# print(fib(6))

def fib_efficient(n,d):
	if n in d:
		return d[n]
	else:
		ans = fib_efficient(n-1,d) + fib_efficient(n-2,d)
		d[n] = ans
		return ans

d = {1:1,2:1}

a=int(input("enter a number: "))

print(fib_efficient(a,d))





