#10 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que
#calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
#atual:
#A. salários até R$ 280,00 (incluindo) : aumento de 20%
#B. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#C. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#D. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#E. o salário antes do reajuste;
#F. o percentual de aumento aplicado;
#G. o valor do aumento;
#H. o novo salário, após o aumento.


salario_atual = float(input("Digite o salário atual do colaborador: R$"))


faixas_reajuste = [
    (280, 0.20),
    (700, 0.15),
    (1500, 0.10),
    (float("inf"), 0.05)
]

reajuste_percentual = None
for faixa, percentual in faixas_reajuste:
    if salario_atual <= faixa:
        reajuste_percentual = percentual
        break


valor_aumento = salario_atual * reajuste_percentual
novo_salario = salario_atual + valor_aumento


print(f"Salário antes do reajuste: R${salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {reajuste_percentual * 100:.2f}%")
print(f"Valor do aumento: R${valor_aumento:.2f}")
print(f"Novo salário após o aumento: R${novo_salario:.2f}")
