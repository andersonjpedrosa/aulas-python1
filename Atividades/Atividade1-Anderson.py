# 1.Help Desk

print("1.Help Desk \nPreencha as informações solicitadas")

# Mensagem de boas-vindas com interpolação e nome em maiúsculas
nome = input("Nome completo: ")
print("Seja bem-vindo(a)", nome.upper())

# Convertendo para int a variavel
ticket = int(input("Nº do ticket: "))

problema = input("Descrição do Problema: ")

# Mostrando o tipo da variavel
print("Tipo da variável do ticket: ", type(ticket))

#Quantidade de caracteres do problema
print("Quantidade de caracteres do problema: ", len(problema) )
print("\n")

#------------------------------

# 2.Alimentos e Bebidas

print("2.Alimentos e Bebidas \nPreencha as informações solicitadas")

drinkprato = input("Nome do Drink ou Prato: ")
qtdepadrao = input("Quantidade padrão em ml/gramas do ingrediente principal por porção: ")
qtdepessoas = input("Quantidade de pessoas que serão servidas: ")

# Convertendo as entradas do usuário
# Quantidade de ingredientes necessários
qtdetotal = float(qtdepadrao) * int(qtdepessoas)

# Dicionário com os dados digitados
dicionario = {
    "Drink/Prato": drinkprato,
    "Total de Ingredientes": qtdetotal
}
print(dicionario)
print("\n")

#------------------------------

# 3.Logística

print("3.Logística \nPreencha as informações solicitadas")

entregas = input("Quantidade de entregas por dia: ")
valorentrega = input("Valor por entrega: ")
valorcombustivel = input("Valor gasto por combustível: ")

# Ganho bruto
ganhobruto = float(valorentrega) * int(entregas)

# Ganho líquido
ganholiquido = ganhobruto - float(valorcombustivel)

# Mensagem com ganho líquido formatado
print("Ganho Líquido:", float(ganholiquido))
print("\n")

#------------------------------

# 4.Autônomo (Gestão de Atividades)

print("4.Autônomo (Gestão de Atividades) \nPreencha as informações solicitadas")

nomeservico = input("Nome do serviço: ")
valorservico = input("Valor total cobrado pelo serviço: ")
horastrab = input("Total de horas trabalhadas: ")

# Valor ganho por hora
print("Valor ganho por hora:",float(valorservico) / float(horastrab))

# Tarefas - Lista (list)
tarefas = ["Comprar Produto 1","Comprar Produto 2","Cadastrar Produto 1","Cadastrar Produto 2"]
print ("Lista de tarefas:", tarefas)

# Status fixos - Tupla (tuple)
status = ("Aprovado","Pendente Pagamento","Em Andamento","Enviado","Devolvido","Entregue","Finalizado")
print ("Status Fixos:", status)