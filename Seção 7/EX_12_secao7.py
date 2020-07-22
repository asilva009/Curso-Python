vet = []
soma = 0
media = 0
print('Digite 5 números: ')
for i in range(5):
    numero = float(input())
    vet.append(numero)
    soma = soma + numero
for valor in vet:
    print(valor)
print(f'Maior= {max(vet)}')
print(f'Menor= {min(vet)}')
print(f'Média= {soma / 5:.1f}')
