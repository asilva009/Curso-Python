class Quadrado:

    def __init__(self, lado):
        self.__lado = lado
        self.__area = self.calcular_area()
        self.__perimetro = self.calcular_perimetro()

    def calcular_area(self):
        return self.__lado * self.__lado

    def calcular_perimetro(self):
        return self.__lado * 4

    def imprimir(self):
        return f'O quadrado de lado {self.__lado} tem área {self.__area} e perimetro {self.__perimetro}'


q1 = Quadrado(5)
print(q1.imprimir())  # O quadrado de lado 5 tem área 25 e perimetro 20






