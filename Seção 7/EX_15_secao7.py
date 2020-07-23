vet = []

print('Digite 20 números: ')
for i in range(20):
    numero = int(input())
    vet.append(numero)
sem_repetidos = set(vet)
for valor in sem_repetidos:
    print(valor)




