salario = float(input("Digite o salário: "))
prestacao = float(input("Valor da parcela do empréstimo: "))
if prestacao > 2 * salario / 10:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
