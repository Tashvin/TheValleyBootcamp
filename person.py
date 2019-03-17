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


class Person(Animal):

	def __init__(self,name,age,height,weight,color,job,school,university):
		Animal.__init__(self,name,age,height,weight,color)
		self.job = job
		self.school = school
		self.university = university
		self.friends = []


	def speak(self):
		return "****Hello*******"

	def get_friends(self):
		return self.friends

	def add_friend(self,fname):
		if fname not in self.friends:
			self.friends.append(fname)

	def age_diff(self,other):
		diff = self.age - other.age
		print(abs(diff), "year difference")


john = Person('john',25,5,70,'brown','se','NP','VTU')
jagan = Person('Jagan',25,5,70,'brown','se','NP','VTU')
# lion = Animal('lion',23,4,5,'blue')
# lion = Person.add_friend("john")

john.add_friend("Loosu")
print(john.friends)

john.age_diff(jagan)

