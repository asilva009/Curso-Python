vet = []
qtde = 0
soma = 0
print('Digite 10 números: ')
for i in range(10):
    numero = float(input())
    vet.append(numero)
for valor in vet:
    if valor < 0:
        qtde = qtde + 1
    else:
        soma = soma + valor
print(f'Quantidade de números negativos = {qtde}')
print(f'Soma dos números positivos = {soma}')
