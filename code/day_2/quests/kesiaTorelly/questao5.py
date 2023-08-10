#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
#porcentagem e custo, que é o custo de #um item #antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    custo_com_imposto = custo + (custo * taxaImposto / 100)
    return custo_com_imposto

custo_item = float(input("Digite o custo do item: "))
taxa_imposto = float(input("Digite a taxa de imposto (%): "))


custo_com_imposto = somaImposto(taxa_imposto, custo_item)



print(f"O custo do item com imposto é: R${custo_com_imposto:.2f}")

