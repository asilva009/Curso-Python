vet = []
contador = 0
print('Digite 10 números: ')
for i in range(10):
    numero = int(input())
    vet.append(numero)
for valor in vet:
    if valor % 2 == 0:
        contador = contador + 1
print(f'Foram digitados {contador} números pares.')
