qtde = 0
numeros = []
numeros_quadrado = []
print('Digite 10 numeros: ')
while qtde < 10:
    numero = float(input())
    numero_quadrado = numero * numero
    numeros.append(numero)
    numeros_quadrado.append(numero_quadrado)
    qtde = qtde + 1
conj_numeros = set(numeros)
conj_quadrados = set(numeros_quadrado)
print(conj_numeros)
print(conj_quadrados)




