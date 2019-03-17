from pers import Person

class Student(Person):
	def __init__(self,age,name,language,subject):
		Person.__init__(self,name,age,language)
		self.subject = subject