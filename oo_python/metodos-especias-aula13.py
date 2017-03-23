class Conta:
	def __init__(self, ID, saldo):
		self.ID = ID
		self.saldo = saldo

	def __str__(self):
		return 'ID: %i\nSaldo: R$ %.2f' %(self.ID, self.saldo)

	def __add__(self, outro):
		self.saldo += outro.saldo 

conta = int(input('id:'))
salario = float(input('salario:'))

Bradesco = Conta(conta, salario)

Itau = Conta(555, 10000)
print(Itau)

Itau + Bradesco
print(Itau.saldo)

conta = int(input('id:'))
salario = float(input('salario:'))

Bradesco = Conta(conta, salario)

print(Bradesco)