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

#Rex.falar()
#Rex.andar()
#Rex.amamentar()

class Pessoa(Animal):
	def __init__(self, cor, genero, andar, cabelo):
		super(Pessoa, self).__init__(cor, genero, andar)
		self.cabelo = 'Castanho'

	def cor_cabelo(self):
		print('A cor do cabelo é {}'.format(self.cabelo))

	def falar(self):
		super(Pessoa, self).falar()# Se deixar desta forma a classe pessoa executa o metodo falar das 2 classes tanto a classe Pessoa quanto a classe Animal.
		print('Olá sou uma pessoa e sei falar')

Gabriel = Pessoa('branco', 'masculino', 2, 'castanho')

Gabriel.andar()
Gabriel.amamentar()
Gabriel.cor_cabelo()
Gabriel.falar()# Quando executado esse comando com o super no metodo falar ele executa ambos os metodos das classes la referenciadas.