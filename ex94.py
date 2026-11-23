frase = input("Digite uma frase: ")

letras_validas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
resultado = ""

for caractere in frase:
    if caractere in letras_validas:
        resultado += caractere
    else:
        resultado += "-"

print("\nResultado:", resultado)