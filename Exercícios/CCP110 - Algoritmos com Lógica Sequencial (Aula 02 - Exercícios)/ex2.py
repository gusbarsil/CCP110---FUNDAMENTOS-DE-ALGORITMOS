km = int(input("Digite a quantidade de quilômetros percorridos: "))
dias = int(input("Digite quantos dias você ficou com o carro: "))
formula = (km * 0.15) + (dias * 60)
print(f"Total a pagar: {formula:.2f}")