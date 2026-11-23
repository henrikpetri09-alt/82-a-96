numeros = []

for i in range(21):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

impares = sorted(numero for numero in numeros if numero % 2 != 0)

if len(impares) == 0:
    print("Todos são pares.")
else:
    print("Existem números ímpares")
    print("Números ímpares em ordem crescente:", impares)