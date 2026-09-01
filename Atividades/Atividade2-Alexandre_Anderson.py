# limpar o terminal
import subprocess
import os

comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)

# -----------------------------------------------
 
# Exercício 1 - Manicure 
print("Manicure \nPreencha os dados a seguir!")
nome = input("Nome: ")
qtde_unhas_decoradas = int(input("Quantidade de unhas decoradas: "))
valor = float(30)
valor_unha_decorada = float(2)
valor_total = valor + (qtde_unhas_decoradas * valor_unha_decorada)

print(f"Olá {nome.upper()}, seja bem-vindo(a)!")
print(f"O valor total a pagar é R${valor_total}")
print(f"Quantidade de caracteres do nome digitado: {len(nome)}")


# Exercício 2 - Lava a Jato
print("\nLava a Jato \nPreencha os dados a seguir!")
nome1 = input("Nome: ")
lavagem_s = float(25)
lavagem_c = float(50)
 
print(f"Olá {nome1.capitalize()}, seja bem-vindo(a)!")
tipo_lavagem = int(input("Digite o serviço (1 para Lavagem Simples / 2 para Lavagem Completa): "))
 
if tipo_lavagem == 1:
    print("Lavagem Simples o valor é de R$", lavagem_s )
elif tipo_lavagem == 2:
    print("Lavagem Completa o valor é de R$", lavagem_c )
else:
    print("Erro")


# Exercício 3 - Estacionamento Pago 
print("\nEstacionamento Pago \nPreencha os dados a seguir!")
valor_hora = float(5)
nome_motorista = input("Nome do motorista: ")
horas_estacionadas = float(input("Quantidade de horas estacionadas: "))
valor_total = valor_hora * horas_estacionadas
desconto = float(0.1) #Desconto de 10%
valor_com_desconto = valor_total - (valor_total * desconto)

if valor_total > 30:
    print(f"Olá {nome_motorista.capitalize()}, você recebeu um desconto de 10%, o valor total a pagar é: R${valor_com_desconto}")
else:
    print(f"Olá {nome_motorista.capitalize()}, o valor total a pagar: R${valor_total}")


# Exercício 4 - Escola Infantil
print("\nEscola Infantil \nPreencha os dados a seguir!")
nome_criança = input("Nome da criança: ")
idade_criança = int(input("Idade da criança: "))
 
if idade_criança < 3:
    print("Fora da faixa atendida")
elif idade_criança <= 4:
    print("Maternal")
elif idade_criança <= 6:
    print("Jardim")
elif idade_criança <= 8:
    print("Pré-escola")
else:
    print("Fora da faixa atendida")
 
print(f"Olá {nome_criança.upper()}")
print(f"Olá {nome_criança.lower()}")
print(f"Seu nome tem ", len(nome_criança), "de caracteres" )


# Exercício 5 - Pastelaria
print("\nPastelaria \nPreencha os dados a seguir!")
valor_queijo = float(8)
valor_carne = float(9)
qtde_queijo = int(input("Quantidade de pastéis de queijo: "))
qtde_carne = int(input("Quantidade de pastéis de carne: "))
qtde_total = qtde_carne + qtde_queijo
total_valor_queijo = valor_queijo * qtde_queijo
total_valor_carne = valor_carne * qtde_carne
total_valor = total_valor_carne + total_valor_queijo

print(f"O valor total da compra é R${total_valor}")
print(f"Quantidade total de pastéis vendidos: {qtde_total}")
if qtde_total > 10:
    print(f"O cliente comprou mais de 10 pastéis")
else:
    print(f"O cliente comprou menos de 10 pastéis")


# Exercício 6 - Casa de Tintas 
print("\nCasa de Tintas")
cores = [ "Azul", "Branco", "Verde", "Amarelo"]

if "Verde" in cores:
    print("A cor Verde está disponível ")
else:
    print("A cor Verde está indisponível ")
 
cores.sort()
print("A ordem das cores é ", cores)
print("A quantidade de cores é ", len(cores))