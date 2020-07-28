vet = []
multiplos = []
contador = 0
for i in range(10):
    numero = int(input(f'Digite o número {i+1}/10: '))
    vet.append(numero)
numero = int(input('Entre os números digitados, mostre os múltiplos de: '))
for valor in vet:
    if valor % numero == 0:
        contador = contador + 1
        multiplos.append(valor)
if contador == 0:
    print(f'\nNão existem múltiplos de {numero}')
else:
    print(f'\nExistem {contador} múltiplos de {numero} \nSão os seguintes:')
    for valor in multiplos:
        print(valor)
