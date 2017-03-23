"""
try:
	x = int(input('Digite um numero: '))
except:
	print('Valor inválido')
	x = 0
finally:
	print(x)
"""

class ValorRepetidoError(Exception):

	def __init__(self, n):
		self.num = n


	def __str__(self):
		return 'Vixe! voce ja digitou este valor {} antes'.format(self.num)

def main():
	lista = []

	for i in range(0, 3):
		while True:
			try:
				num = int(input('Digite um numero: '))
				break
			except ValueError:
				print('Digite apenas numeros')

		if num not in lista:
			lista.append(num)
		else:
			raise ValorRepetidoError(num)

main()

