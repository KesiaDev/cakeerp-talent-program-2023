#- Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def calcular_soma(a, b, c):
    soma = a + b + c
    return soma


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


resultado = calcular_soma(num1, num2, num3)


print(f"A soma dos três números é: {resultado}")
