contador = 0
vet = []
print('Digite alguns números: ')
while contador < 6:
    nun = int(input())
    if nun % 2 == 0:
        vet.append(nun)
        contador = contador + 1
vet.reverse()
print('Abaixo estão, de forma inversa, os 6 numeros pares digitados')
for valores in vet:
    print(valores)


