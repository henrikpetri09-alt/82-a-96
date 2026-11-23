vetor1 = []
vetor2 = []

print("Digite 10 valores para o primeiro vetor:")
for i in range(10):
    valor = int(input(f"Valor {i + 1}: "))
    vetor1.append(valor)

print("\nDigite 12 valores para o segundo vetor:")
for i in range(12):
    valor = int(input(f"Valor {i + 1}: "))
    vetor2.append(valor)

valores_comuns = sorted(set(vetor1) & set(vetor2), reverse=True)

print("\nValores comuns em ordem decrescente:", valores_comuns)