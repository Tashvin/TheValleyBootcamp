class Animal:

	def __init__(self,name,age,height,weight,color):
		self.age = age
		self.name = name
		self.height = height
		self.weight = weight
		self.color = color

	def __str__(self):
		return "animal: " + str(self.name) + ":" + str(self.age)


	def speak(self):
		return "*****sounds*****"


# lion = Animal('lion',15,6,70,"brown")
# print(lion.age,lion.name,lion.height,lion.weight)
# print(lion)
# print(lion.speak())
# 		