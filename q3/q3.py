#Wanessa Alves
class Circulo:

	def __init__(self, raio, area = "", perimetro=""):
		self.raio = raio
		self.area = area
		self.perimetro = perimetro

	def calcularArea(self):
		self.area = round(3.141516*self.raio*self.raio,4)
		print("A area é {}".format(self.area))

	def calcularPerimetro(self):
		self.perimetro = round(2*3.141516*self.raio,4)
		print("O perimetro é {}".format(self.perimetro))

	def imprimir(self):
		print("Raio: {}".format(self.raio))
		print("Area: {}".format(self.area))
		print("Perimetro: {}".format(self.perimetro))