class Pessoa:

    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir(self):
        return f'Nome: {self.__nome}\nEndereço: {self.__endereco}\nTelefone: {self.__telefone}'
    


pessoa1 = Pessoa('Alexandre', 'Rua Almada, 32 - São Paulo/SP', 932123455)
pessoa2 = Pessoa('José', 'Rua Atabasca, 12 - Santo André/SP', 987653456)

print(pessoa1.imprimir())
print(pessoa2.imprimir())





