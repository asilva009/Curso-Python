vet = []
print('Digite 10 números: ')
for i in range(10):
    numero = int(input())
    vet.append(numero)
print(f'Vetor criado = {vet}')
print(f'O maior elemento deste vetor é o {max(vet)} e ele se encontra na posição {vet.index(max(vet))}')

