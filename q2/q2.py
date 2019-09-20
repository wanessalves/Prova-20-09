#Wanessa Alves
class Quadrado:

	def __init__(self, lado, area="", perimetro=""):
		self.lado = lado
		self.area = area
		self.perimetro = perimetro

	def calcularPerimetro(self):
		self.perimetro = self.lado*4
		print("O perimetro é {}".format(self.perimetro))

	def calcularArea(self):
		self.area = self.lado * self.lado
		print("A area é {}".format(self.area))

	def mostrarValores(self):
		print("O valor do Quadrado é {}, o Perimetro é {} e a Area é {}!!!".format(self.lado, self.area, self.perimetro))	