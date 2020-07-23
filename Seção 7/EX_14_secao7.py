vet = []
repete = []
print('Digite 10 números: ')
for i in range(10):
    numero = int(input())
    if numero in vet and numero not in repete:
        repete.append(numero)
    vet.append(numero)
for valor in repete:
    print(f'O valor {valor} repete na lista {vet.count(valor)} vezes.')



