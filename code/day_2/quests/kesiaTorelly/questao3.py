#3 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#A. "Telefonou para a vítima?"
#B. "Esteve no local do crime?"
#C. "Mora perto da vítima?"
#D. "Devia para a vítima?"
#E. "Já trabalhou com a vítima?"

# Inicializando a lista de perguntas

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]


respostas = []


for pergunta in perguntas:
    resposta = input(f"{pergunta} (Sim ou Não): ")
    respostas.append(resposta.lower()) 


suspeita = False

if respostas.count("sim") >= 3:
    suspeita = True

if suspeita:
    print("Você é considerado um(a) suspeito(a) do crime.")
else:
    print("Você não é considerado um(a) suspeito(a) do crime.")
