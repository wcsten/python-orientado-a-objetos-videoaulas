class Meu_Objeto:
    def __init__(pessoa, nome, idade): #função que inicia o objeto cria o objeto
        pessoa.nome = nome
        pessoa.idade = idade
        print('Chamando o construtor')

    def imprime(pessoa): #função para imprimir os atributos do objeto criado acima
        print('Olá meu nome é {} e eu tenho {} anos'.format(pessoa.nome, pessoa.idade))


Jorge = Meu_Objeto('Jorge', 20)

Jorge.imprime()