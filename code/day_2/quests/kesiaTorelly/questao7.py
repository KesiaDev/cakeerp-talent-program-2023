#- Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite a letra correspondente ao gênero (F para Feminino, M para Masculino): ")


if letra == "F" or letra == "f":
    print("F - Feminino")
elif letra == "M" or letra == "m":
    print("M - Masculino")
else:
    print("Sexo Inválido")
