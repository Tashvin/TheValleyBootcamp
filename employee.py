from student import Student

class Employee(Student):
	def __init__(self,age,name,language,company):
		Student.__init__(self,age,name,language)
		self.company = company