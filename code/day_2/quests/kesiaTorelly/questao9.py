#9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


numeros = [num1, num2, num3]


numeros.sort(reverse=True)


print("Números em ordem decrescente:")
for numero in numeros:
    print(numero)

