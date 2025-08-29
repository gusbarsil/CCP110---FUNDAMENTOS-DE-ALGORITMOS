salario = float(input("Digite seu salário: "))

if salario > 1250:
    salarioNovo = (salario*1.1)
    print(f"{salarioNovo:.2f}")
else:
    salarioNovo = (salario*1.15)
    print(f"{salarioNovo:.2f}")