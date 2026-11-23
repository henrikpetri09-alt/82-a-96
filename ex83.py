numeros = []

for i in range(18):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

print("\nNúmeros em ordem inversa:")
for numero in reversed(numeros):
    print(numero)