def operacoes_matematicas(num1, num2, simbolo ):
    if simbolo == '+':
        return f'Soma = {num1 + num2}'
    elif simbolo == '-':
        return f'Subtração = {num1 - num2}'
    elif simbolo == '/':
        return f'Divisão = {num1 / num2:.2f}'
    return f'Multiplicação = {num1 * num2}'
