#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem
#lida.


idades = []
alturas = []


for i in range(5):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    altura = float(input(f"Digite a altura da {i+1}ª pessoa (em metros): "))
    
    idades.append(idade)
    alturas.append(altura)


print("\nIdades e alturas na ordem inversa:")
for i in range(4, -1, -1):
    print(f"Idade: {idades[i]} anos, Altura: {alturas[i]:.2f} metros")
