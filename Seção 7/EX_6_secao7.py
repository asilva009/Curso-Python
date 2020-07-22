vet = []
print('Digite 10 números: ')
for i in range(10):
    numero = int(input())
    vet.append(numero)
print(f'O menor número digitado é {min(vet)} e o maior é {max(vet)}.')
