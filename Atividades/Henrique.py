print ("Exercício 1 - Pet Shop - Cálculo de banho")
while True:
    nomedopet = input('Informe o nome do seu pet: ')
    if nomedopet.isalpha():
        break
    else:
        print('Erro! Digite apenas letras do nome do seu pet <3.')
while True:
    kg_input = input('Qual o peso do seu pet? (Em KG) ')
    if kg_input.strip() == "":
        print("Entrada vazia. Digite apenas números (ex.: 5).")
        continue
    try:
        lavagem = int(kg_input)
        break
    except ValueError:
        print("Digite apenas números inteiros porfavor (não use letras).")
if lavagem <= 10:
    valorapagar = 30.0
    print(f'{nomedopet.upper()} ')
    print(f'Vai ser uma lavagem mais simples então o valor a pagar será R$ {valorapagar}.')
elif lavagem >= 11 <= 20:
    valorapagar = 50.0
    print(f'{nomedopet.upper()} ')
    print(f'Pelo seu animal ser de um pouco mais grande o valor a pagar será R$ {valorapagar}.')
elif lavagem > 20:
    valorapagar = 70.0
    print(f'{nomedopet.upper()} ')
    print(f'Pelo seu animal ser de grande porte o valor a pagar será R$ {valorapagar}.')
else:
    print("Não atendemos animais tão grande, porfavor volte sempre")
print("preço total do serviço: R$",valorapagar)

print(f'\n')

input('Digite ENTER para continuar')

import subprocess
import os

comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)

print("Exercício 2 - Empresa de Frota de Motos - Controle de Quilometragem")
while True:
    quantidadedemotos = input('Informe o número de motos da sua frota: ')
    if quantidadedemotos.isdigit():
        break
    else:
        print('Erro! Digite apenas números.')
quantidadedemotos = int(quantidadedemotos)
kms = []
if quantidadedemotos >= 2:
    for i in range(1, quantidadedemotos + 1):
        while True:
            km_input = input(f"Quantos Km a moto {i} registrou? ").strip()
            if km_input == "":
                print("Entrada vazia. Digite apenas números.")
                continue
            if km_input.isdigit():
                km = int(km_input)
                break
            else:
                print("Erro! Digite apenas números inteiros")
        kms.append(km)
elif quantidadedemotos == 1:
    while True:
        km_input = input("Quantos Km a sua moto registrou? ").strip()
        if km_input == "":
            print("Entrada vazia. Digite apenas números.")
            continue
        if km_input.isdigit():
            km = int(km_input)
            break
        else:
            print("Erro! Digite apenas números inteiros")
    kms.append(km)

ValorTotal = sum(kms)
print(f"O seu total de Km que vc percorreu foi: {ValorTotal} Kms")
print(f"A sua média foi: {ValorTotal/quantidadedemotos:.2f} Kms percorridos")


print(f'\n')

input('Digite ENTER para continuar')

import subprocess
import os

comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)

print("Exercício 3 - Lanchonete de Hot Dog - Pedido do Cliente")
HotDogSimples = 10
HotDogDuplo = 15
CocaCola = 6
Pepsi = 6

while True:
    Hotdogs = input('Qual o seu nome?: ')
    if Hotdogs.isalpha():
        break
    else:
        print('Erro! Digite apenas letras do seu nome.')

print("Boas vindas", Hotdogs, "a nossa loja de hotdog, temos dois tipos de hotdogs e refrigerantes")
total = 0
quantidadesimples = 0
quantidadeduplo = 0
quantidadecoca = 0
quantidadepepsi = 0
while True:
    try:
        escolha = int(input('Qual HotDog ou Refri você quer? 1 = HotDog Simples, 2 = HotDog Duplo, 3 = Coca-Cola, 4 = Pepsi: '))
    except ValueError:
        print("Por favor digite um número entre 1 e 4.")
        continue
    if escolha == 1:
        try:
            quantidadesimples = int(input("E quantos HotDogs Simples vc vai querer? "))
        except ValueError:
            print("Quantidade errada, voltando ao menu.")
            continue
        if quantidadesimples <= 0:
            print("Quantidade deve ser maior que zero.")
        else:
            total += quantidadesimples * HotDogSimples
            print(f"{quantidadesimples}x Hot Dog Simples adicionados. Subtotal atual: R$ {total:.2f}")
    elif escolha == 2:
        try:
            quantidadeduplo = int(input("E quantos HotDogs Duplos vc vai querer? "))
        except ValueError:
            print("Quantidade errada, voltando ao menu.")
            continue
        if quantidadeduplo <= 0:
            print("Quantidade deve ser maior que zero.")
        else:
            total += quantidadeduplo * HotDogDuplo
            print(f"{quantidadeduplo}x Hot Dog Duplo adicionados. Subtotal atual: R$ {total:.2f}")
    elif escolha == 3:
        try:
            quantidadecoca = int(input("E quantas Coca-Colas vc vai querer? "))
        except ValueError:
            print("Quantidade errada, voltando ao menu.")
            continue
        if quantidadecoca <= 0:
            print("Quantidade deve ser maior que zero.")
        else:
            total += quantidadecoca * CocaCola
            print(f"{quantidadecoca}x Coca-Cola adicionadas. Subtotal atual: R$ {total:.2f}")
    elif escolha == 4:
        try:
            quantidadepepsi = int(input("E quantas Pepsi vc vai querer? "))
        except ValueError:
            print("Quantidade errada, voltando ao menu.")
            continue
        if quantidadepepsi <= 0:
            print("Quantidade deve ser maior que zero.")
        else:
            total += quantidadepepsi * Pepsi
            print(f"{quantidadepepsi}x Pepsi adicionadas. Subtotal atual: R$ {total:.2f}")
    else:
        print("Opção errada my friend, Escolha entre 1 e 4 pls.")
        continue
    while True:
        try:
            opc = int(input("Vc vai querer mais alguma coisa? Digite 1 para sim e 2 para fechar a conta e ir para o pagamento: "))
        except ValueError:
            print("Digite 1 para sim ou 2 para fechar.")
            continue
        if opc in (1, 2):
            break
        print("Digite 1 para sim ou 2 para fechar.")

    if opc == 2:
        break
print()
if total == 0:
    print("Nenhum item no pedido. Até logo!")
else:
    if total > 50:
        desconto = total * 0.10
        total_com_desconto = total - desconto
        print(f"O seu valor total deu R$ {total:.2f}")
        print(f"Você ganhou 10% de desconto: -R$ {desconto:.2f}")
        print(f"Total a pagar com desconto: R$ {total_com_desconto:.2f}")
    else:
        print(f"O seu valor total deu R$ {total:.2f}")

input('Digite ENTER para continuar')

import subprocess
import os

comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)


print("Exercício 4 - Consultoria de Segurança do Trabalho - Avaliação de Risco")
while True:
    nomedocliente = input('Informe o nome do cliente: ')
    if nomedocliente.isalpha():
        break
    else:
        print('Erro! Digite apenas letras.')
print("Boas vindas ", nomedocliente,"espero que possamos ajudar vc")
while True:
    try:
        risco = int(input('De 0 a 10, qual a sua escala de risco? '))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro entre 0 e 10.")
        continue
    if 0 <= risco <= 10:
        break
    else:
        print("Número fora do intervalo. Digite um valor entre 0 e 10.")
if risco >= 0 and risco <= 3:
   nivel = 'O seu nivel de risco e Baixo, vamos proseguir com mais calma a papelada'
elif risco >= 4 and risco <= 7:
   nivel = 'O seu nivel de risco e Médio, vamos agilizar um pouco a papelada'
elif risco >= 8 and risco <= 10:
   nivel = 'O seu nivel de risco e Alto, vamos fazer a papelada com urgencia!'
else:
   nivel = 'O nivel que vc digitou é invalido, digite o nivel de risco novamente entre 0 a 10'
print(nivel)   
print("Esperamos que tenhamos ajudado vc com seu nivel de risco volte sempre")

print(f'\n')

input('Digite ENTER para continuar')

import subprocess
import os

comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)

print("Exercício 5 - Empresa de Limpeza - Controle de Equipes") 
while True:
    quantidadedepessoas = input('Informe a quantidade de pessoas que você ira cadastrar na sua equipe:')
    if quantidadedepessoas.isdigit():
        break
    else:
        print('Erro! Digite apenas números porfavor.')
quantidadedepessoas = int(quantidadedepessoas)
quantidadedeoperarios = []
if quantidadedepessoas >= 2:
    for i in range(1, quantidadedepessoas + 1):
        while True:
            pessoa = input(f"Qual o nome da {i} pessoa da sua equipe? ").strip()
            if pessoa.isalpha():
                quantidadedeoperarios.append(pessoa)
                break
            else:
                print("Erro, apenas letras porfavor, tente novamente")
elif quantidadedepessoas == 1:
    while True:
        pessoa = input("Qual o nome da pessoa que você quer registrar? ").strip()
        if pessoa.isalpha():
            quantidadedeoperarios.append(pessoa)
            break
        else:
            print("Erro, apenas letras porfavor, tente novamente")
ValorTotal = len(quantidadedeoperarios)

print(f"O total de funcionarios registrados foram: {ValorTotal}")
print(f"Os seguintes nomes foram registrado no nosso banco de dados de equipes: {quantidadedeoperarios}")

nomes_ordenados = sorted(quantidadedeoperarios)
print(f"Nomes em Ordem Alfabetica: {nomes_ordenados}")

print(f'\n')

input('Digite ENTER para continuar')


import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

resp = requests.get(URL, timeout=10)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

for book in books:
    a_tag = book.find("h3").find("a")
    title = a_tag.get("title", "").strip()
    price_tag = book.find("p", class_="price_color")
    price = price_tag.text.strip() if price_tag else ""
    print(f"Título: {title}  |  Preço: {price}")


print(f'\n')

input('Digite ENTER para continuar')

import subprocess
import os

comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)