vet = []
print('Digite 5 números: ')
for i in range(5):
    numero = float(input())
    vet.append(numero)

print(f'Maior valor está na posição {vet.index(max(vet)) + 1}')
print(f'Menor valor está na posição {vet.index(min(vet)) + 1}')
