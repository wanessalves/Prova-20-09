#Wanessa Alves
class Moto:

	def __init__(self, marca, modelo, cor, marcha, menorMarcha=0, maiorMarcha=4, ligada=""):
		self.marca = marca
		self.modelo = modelo
		self.cor = cor
		self.marcha = marcha
		self.menorMarcha = menorMarcha
		self.maiorMarcha = maiorMarcha
		self.ligada = ligada

	def imprimir(self):
		print("===============================")
		print("Marca da Moto: {}".format(self.marca))
		print("Modelo da Moto: {}".format(self.modelo))
		print("Cor da Moto: {}".format(self.cor))
		print("Marcha atual da Moto: {}".format(self.marcha))
		print("Estado da Moto: {}".format(self.ligada))
		print("===============================")

	def baixarMacha(self):
		if(self.marcha > self.menorMarcha):
			self.marcha = self.marcha - 1
			print("Marcha atual: {}".format(self.marcha))
		else:
			print("Você está no Neutro")	

	def subirMacha(self):
		if(self.marcha < 4 and self.marcha > self.menorMarcha):
			self.marcha = self.marcha + 1
			print("Marcha atual: {}".format(self.marcha))
		else:
			print("Você está de quarta, baixe a marcha!!")

	def status(self, valor):
		if(valor == "ligada"):
			return True
			self.ligada = status()
		print(self.ligada)

		else:
			print("Desligada")			