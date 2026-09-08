# limpar o terminal
import subprocess
import os

comando = "cls" if os.name == "nt" else "clear"
def limpar():
    subprocess.run(comando, shell=True)

limpar() 
#------------------------------------------------------------------------------- 
# Exercício 1 - Pet Shop 
print("Exercício 1 - Pet Shop")

def calcular_banho(peso):
    if peso <= 10:
        return 30
    elif peso <= 20:
        return 50
    else:
        return 70

nome_pet = input("Digite o nome do seu Pet: ")

while True:

    peso_pet = input("Digite o peso do seu Pet (em kg): ")
    try:
        peso_pet = float(peso_pet)
        break
    except ValueError:
        print("Erro! Digite um peso válido (ex.: 5 ou 10.2)")

print(f"Nome do Pet: {nome_pet}")
valor = calcular_banho(peso_pet)
print(f"Valor do Banho: R${valor:.2f}")


print("\n")
input("Aperte ENTER para continuar...")
limpar()
#-------------------------------------------------------------------------------
# Exercício 2 - Frota de Motos
print("Exercício 2 - Frota de Motos")
qtde_motos = int(input("Digite a quantidade de motos da frota: "))
km_total = 0
maior_km = 0

for m in range(1, qtde_motos + 1):
    km_moto = float(input(f"Qual a quilometragem percorrida pela moto {m}: "))
    km_total = km_total + km_moto

    if km_moto > maior_km:
        maior_km = km_moto
    
media_km = km_total / qtde_motos
print(f"Total de quilômetros percorrido pela frota: {km_total:.2f}km")
print(f"Média de quilômetros por moto: {media_km:.2f}km")
print(f"A maior quilometragem registrada foi de {maior_km:.2f}km")


print("\n")
input("Aperte ENTER para continuar...")
limpar() 
#-------------------------------------------------------------------------------
# Exercício 3 - Lanchonete de Hot Dog
print("Exercício 3 - Lanchonete de Hot Dog")

cardapio = {
    "Hot Dogs Simples":10.00,
    "Hot Dogs Duplos":15.00,
    "Refrigerantes": 6.00
}

print ("Cardápio:\nHot Dog Simples: R$10,00\nHot Dog Duplo: R$15,00\nRefrigerante: R$6,00")

valor_total = 0

for item, preco in cardapio.items():
    qtde = int(input(f"Quantos(as) {item} deseja comprar? R: "))
    valor_compra = qtde * preco
    valor_total = valor_total + valor_compra

desconto = float(0.9) # 0.9 representa um desconto de 10%
valor_com_desconto = valor_total * desconto

if valor_total > 50:
    print(f"Você recebeu um desconto de 10%. O valor total da compra é R${valor_com_desconto:.2f}")
else:
    print(f"O valor total da compra é R${valor_total:.2f}")


print("\n")
input("Aperte ENTER para continuar...")
limpar() 
#-------------------------------------------------------------------------------
# Exercício 4 - Avaliação de Risco
print("Exercício 4 - Avaliação de Risco")

while True:
    try:
        nota = float(input("Digite uma nota de 0 a 10: "))
        if nota <= 3:
            print(f"Nota {nota} - Risco Baixo")
            break
        elif nota <= 7:
            print(f"Nota {nota} - Risco Médio")
            break
        elif nota <= 10:
            print(f"Nota: {nota} - Risco Alto")
            break
        else:
            print("Erro! Você não digitou uma nota maior que 10. Tente novamente!")
    except ValueError:
        print("Erro! Você não digitou um valor válido. Tente novamente!")


print("\n")
input("Aperte ENTER para continuar...")
limpar() 
#-------------------------------------------------------------------------------
# Exercício 5 - Controle de Equipes
print("Exercício 5 - Controle de Equipes")

def mostrar_funcionarios(equipe):
    print(f"Nomes dos funcionários cadastrados: {equipe}")

print("Digite os nomes dos funcionários da equipe. A cada nome aperte ENTER para incluir o próximo.\nDigite 'fim' para finalizar")

nome_func = ""
equipe = []

while True:
    nome_func = input("Nome: ")
    if nome_func != "fim":
        equipe.append(nome_func)
    else:
        break

qtde_func = len(equipe)
print(f"Quantidade de funcionários cadastrados: {qtde_func}")

mostrar_funcionarios(equipe)


print("\n")
input("Aperte ENTER para continuar...")
limpar()
#-------------------------------------------------------------------------------
# Exercício 6 - BeautifulSoup
print("Exercício 6 - BeautifulSoup")

# Importando as bibliotecas
import requests
from bs4 import BeautifulSoup

pagina = requests.get("https://books.toscrape.com/")
dados_pagina = BeautifulSoup(pagina.text, "html.parser") #pega só os texto em html

info = dados_pagina.find_all(class_="product_pod")



def exibir_dados(dados):
    for produto in dados:

        titulos = produto.find("h3").find("a")["title"]     #procura a tag h3 dentro dela a tag a e dentro o atributo title
        precos = produto.find(class_="price_color").text    #.tex para trazer apenas o texto que tem dentro da tag

        print(f"Título: {titulos} | Preço: {precos}")

exibir_dados(info)