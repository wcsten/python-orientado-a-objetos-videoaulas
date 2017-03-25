class Pessoa(object):

	def __init__(self, name, gender, birth_year, country='Brasil'):
		self.nome = name
		self.sexo = gender
		self.ano_de_nascimento = birth_year
		self.pais = country

	def __str__(self):
		return self.nome

	def __repr__(self):
		return self.nome

	@classmethod
	def alterar_ano_base(cls, year):
		cls.ano = year

	def calcular_idade(self):
		return Pessoa.ano - self.ano_de_nascimento

