class Animal:
	def __init__(self, cor, genero, andar):
		self.cor = cor
		self.genero = genero
		self.num_de_patas = andar

	def falar(self):
		print('Olá sou um cachorro e sei falar')

	def andar(self):
		print('Estou andando sobre {} patas'.format(self.num_de_patas))
	
	def amamentar(self):
		if self.genero.lower() [0] == 'm':
			print('Machos não amamentam')
			return
		print('Amamentando meu filhote')	

Rex = Animal('Preto', 'masculino', 4)	

Rex.falar()
Rex.andar()
Rex.amamentar()

class Pessoa(Animal):
	def __init__(self, cor, genero, andar, cabelo):
		super(Pessoa, self).__init__(cor, genero, andar)
		self.cabelo = 'Castanho'

	def cor_cabelo(self):
		print('A cor do cabelo é {}'.format(self.cabelo))

Gabriel = Pessoa('branco', 'masculino', 2, 'castanho')

Gabriel.andar()
Gabriel.amamentar()
Gabriel.cor_cabelo()