from ani import Animal

class Monkey(Animal):

	def __init__(self,age,name):
		Animal.__init__(self,age)
		self.name = name

		
	def tricks(self):
		return "dance"