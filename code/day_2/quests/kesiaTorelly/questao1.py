#1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.


numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)


print("Os números digitados são:")
for numero in numeros:
    print(numero)
