#input.py

entrada = int(input("Digite a entrada: "))

entrada_teste = entrada > 1 and entrada < (10 ** 3)

if(entrada_teste):
    print("OK")
else:
    print("ERROR")
