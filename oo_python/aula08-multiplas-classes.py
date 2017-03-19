class Animal:
	def __init__(self, cor, genero, andar):
		self.cor = cor
		self.genero = genero
		self.num_de_patas = andar

	def falar(self):
		print('Olá sou um cachorro e sei falar')

	def andar(self):
		print('Estou andando sobre {} tantas patas'.format(self.num_de_patas))
	
	def amamentar(self):
		if self.genero.lower() [0] == 'm':
			print('Machos não amamentam')
			return
		print('Amamentando meu filhote')		