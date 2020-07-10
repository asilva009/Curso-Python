import math
numero = int(input("Digite um número inteiro: "))
if numero > 0:
    logaritmo = math.log(numero)
    print(f"O logaritmo de {numero} é {logaritmo:.3f}")
else:
    print("Número inválido")
