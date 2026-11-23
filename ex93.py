frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
letras_sem_acento = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

quantidade_vogais = 0
quantidade_consoantes = 0
quantidade_outros = 0

for caractere in frase:
    if caractere in vogais:
        quantidade_vogais += 1
    elif caractere in letras_sem_acento:
        quantidade_consoantes += 1
    else:
        quantidade_outros += 1

print(f"\nVogais: {quantidade_vogais}")
print(f"Consoantes: {quantidade_consoantes}")
print(f"Outros caracteres: {quantidade_outros}")