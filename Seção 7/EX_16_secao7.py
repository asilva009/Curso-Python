vet = []
for i in range(5):
    numero = float(input(f'Digite o valor {(i+1)}/5: '))
    vet.append(numero)
codigo = int(input('Digite um código: \n0 - para sair \n1 - para vetor na ordem direta \n2 - para vetor na ordem inversa\n'))

while codigo < 0 or codigo > 2:
    print('Código inválido\n')
    codigo = int(input('Digite um código: \n0 - para sair \n1 - para vetor na ordem direta \n2 - para vetor na ordem inversa'))
if codigo == 1:
    print(vet)
elif codigo == 2:
    vet.reverse()
    print(vet)
else:
    print('FIM')

