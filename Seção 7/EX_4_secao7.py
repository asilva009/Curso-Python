vet = []
soma = 0
print('Digite 8 números: ')
for i in range(8):
    numero = int(input())
    vet.append(numero)
print('Escolha 2 posições entre 0 e 7')
x = int(input())
y = int(input())
soma = vet[x] + vet[y]
print(f'A soma dos números nas respectivas posições é {soma}')


