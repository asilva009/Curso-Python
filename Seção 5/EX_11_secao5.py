soma = 0
print('Digite um número inteiro')
numero = input()
if int(numero) >= 0:
    num = list(numero)
    for number in range(len(num)):
        soma = soma + int(num[number])
    print(f'A soma dos números é {soma}')
else:
    print('Número invalido')

