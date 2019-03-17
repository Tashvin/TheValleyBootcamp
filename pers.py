from monk import Monkey

class Person(Monkey):
	def __init__(self,age,name,language):
		Monkey.__init__(self,age,name)
		self.language = language
