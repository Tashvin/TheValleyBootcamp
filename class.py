# class Pen :

# 	def __init__(self,color,height,diameter):
# 		self.color = color
# 		self.height = height
# 		self.diameter = diameter

# 	def write(self):
# 		return "Hello World"

# 	def change_refill_color(self,color):
# 		self.color = color


# reynolds = Pen('red',12,15)
# reynolds.change_refill_color("blue")
# print(reynolds.write())
# print(reynolds.color)


class Point:

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __add__(other,self):
		return Point(self.x + other.x, self.y + other.y)

	def __str__(self):
		return f"{self.x},{self.y}"

	def distance(self,other):
		xsq = (self.x - other.x) **2
		ysq = (self.y - other.y) **2
		return (xsq + ysq)** 0.5

x = Point(1,2)
y = Point(2,3)

# c = x + y

# print(c.x)
# print(c.y)

# print(x)
# print(y)

#print(x.distance(y))

a = Point(0,0)
b = Point(0,1)
c = Point(1,1)
d = Point(1,0)

class Square:

	def __init__(self,p1,p2,p3,p4):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.p4 = p4


	def area(self):

		side = self.p1.distance(self.p2)
		return side **2

square1 = Square(a,b,c,d)

print(square1.area())		



