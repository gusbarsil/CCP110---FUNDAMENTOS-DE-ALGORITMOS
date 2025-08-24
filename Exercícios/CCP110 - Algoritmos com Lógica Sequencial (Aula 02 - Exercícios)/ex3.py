dias = int(input("Digite os dias: "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

formula = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print("São: " + formula)