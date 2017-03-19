Pessoa = {'Nome': 'Gabriel', 'Profissao': 'Programador', 'Idade': 20}

print(Pessoa ['Nome'])
print(Pessoa ['Profissao'])
print(Pessoa ['Idade'])

class Pessoa:
	pass

Gabriel = Pessoa()

Gabriel.nome = 'Gabriel'
Gabriel.emprego = 'Tudo'
Gabriel.idade = 20

print(Gabriel.__dict__)