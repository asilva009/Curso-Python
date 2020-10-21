class Quadrado:

    def __init__(self, lado):
        self.__lado = lado
        self.__area = self.__lado * self.__lado
        self.__perimetro = self.__lado * 4

    def imprimir(self):
        return f'O quadrado de lado {self.__lado} tem área {self.__area} e perimetro {self.__perimetro}'


q1 = Quadrado(6)
print(q1.imprimir())  # O quadrado de lado 6 tem área 36 e perimetro 24



