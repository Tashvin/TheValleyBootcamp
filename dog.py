from ani import Animal

class Dog(Animal):
	def __init__(self,age,name):
		Animal.__init__(self,age)
		self.name = name

	def play(self):
		return "play"