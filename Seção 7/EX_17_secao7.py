vet = []
for i in range(10):
    numero = int(input(f'Digite o número {i+1}/10: '))
    vet.append(numero)
print(vet)
for valor in vet:
    if valor < 0:
        vet.insert(vet.index(valor), 0)
        vet.pop(vet.index(valor))
print(vet)

