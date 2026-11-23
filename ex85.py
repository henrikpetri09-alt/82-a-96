pessoas = []

for i in range(7):
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    pessoas.append((nome, idade))

print("\nPessoas com 18 anos ou mais:")
for nome, idade in pessoas:
    if idade >= 18:
        print(nome)