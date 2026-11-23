caracteres = []

for i in range(12):
    while True:
        caractere = input(f"Digite o {i + 1}º caractere: ")
        if len(caractere) == 1:
            caracteres.append(caractere)
            break
        print("Digite apenas um caractere.")

for i in range(0, 12, 2):
    caracteres[i], caracteres[i + 1] = caracteres[i + 1], caracteres[i]

print("\nCaracteres após as trocas:")
print(", ".join(caracteres))