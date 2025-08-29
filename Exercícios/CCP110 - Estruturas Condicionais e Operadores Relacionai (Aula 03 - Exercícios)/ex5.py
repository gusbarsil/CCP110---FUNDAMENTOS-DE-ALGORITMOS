anoAtual = int(input("Digite o ano atual: "))
anoNasc = int(input("Digite o ano de nascimento: "))

idade = anoAtual - anoNasc

if idade >= 18:
    print("Você pode tirar a CNH")
    if idade < 18:
        print("Você não pode tirar a carta.")