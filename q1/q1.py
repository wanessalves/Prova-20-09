#Wanessa Alves
class Pessoa:

	def __init__(self, nome, endereço, telefone):
		self.nome = nome
		self.endereço = endereço
		self.telefone = telefone

	def imprimir(self):
		print(self.nome)
		print(self.endereço)
		print(self.telefone)	
