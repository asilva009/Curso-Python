def fatorial(n):
    if n < 0:
        return 'O número deve ser inteiro positivo'
    fat = 1
    for valor in range(1, n+1):
        fat = fat * valor
    return f'{n}! = {fat}'
