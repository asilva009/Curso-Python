class Quadrado:

    area, perimetro = 0, 0

    def __init__(self, lado):
        self.__lado = lado

    def calcular_area(self):
        Quadrado.area = self.__lado * self.__lado

    def calcular_perimetro(self):
        Quadrado.perimetro = self.__lado * 4

    def imprimir(self):
        return f'O quadrado de lado {self.__lado} tem área {Quadrado.area} e perimetro {Quadrado.perimetro}'

q1 = Quadrado(5)
q1.calcular_area()
q1.calcular_perimetro()
print(q1.imprimir())  # O quadrado de lado 5 tem área 25 e perimetro 20






