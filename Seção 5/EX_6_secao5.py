print('Digite dois números inteiros:')
num1 = int(input())
num2 = int(input())
if num1 > num2:
    print(f'{num1} é o maior')
else:
    print(f'{num2} é o maior')
diferenca = (num1 - num2).__abs__()
print(f'A diferença entre os números é {diferenca}')

