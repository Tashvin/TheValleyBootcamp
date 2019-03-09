class Bottle():
	quantity = 100
	shape = 'cylindrical'

	def __init__(self,color,quality,sipper):
		self.color = color
		self.quality = quality
		self.sipper = sipper

	def fill_water(self):
		print("Water for", self.color, "is filled.")

	def change_color(self, new_color):
		print("old color was", self.color)
		self.color = new_color
		print("the color has been changed to", self.color)

bottle1 = Bottle(color = 'red', quality = 'high', sipper = False)
bottle2 = Bottle(color = 'blue', quality = 'low', sipper = True)
#import pdb; pdb.set_trace()