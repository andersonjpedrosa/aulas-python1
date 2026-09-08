import csv  #importa a biblioteca csv

#leitura
def mostrar_lista():
    with open('listaprodutos.csv', 'r') as arquivo: #vai ler o csv
        csv_reader = csv.reader(arquivo, delimiter=';') #vai guardar os dados que foram lidos em uma variavel
        for line in csv_reader:     #vai ler linha a linha o que tem nos dados
            print(line) #imprimir as linhas

#atualizar
dados = []

with open('listaprodutos.csv', 'r', newline='', encoding='utf-8') as arquivo:   #encoding='utf-8' serve para aceitar palavras com acento
    csv_reader = csv.reader(arquivo, delimiter=';') 

    for linha in csv_reader:    
        if linha[0] == "mouse":     #vai verificar se na linha a coluna [] tem o noem mouse
            linha[2] = "35.99"      #se sim substituir pelo novo valor
        dados.append(linha)         #adiciona os dados na lista

with open('listaprodutos.csv', 'w', newline='', encoding='utf-8') as arquivo:
     csv_writer = csv.writer(arquivo, delimiter=';')    
     csv_writer.writerows(dados)    #sobrescreve o valor do arquivo

mostrar_lista()
print("Produto atualizado!")

#adicionar um novo produto
novo_produto = ["fone", 5, f"{49.90:.2f}"]

with open("listaprodutos.csv", "a", newline="", encoding="utf-8") as arquivo:   # a de adicionar (append)
    csv_writer = csv.writer(arquivo, delimiter=";")
    csv_writer.writerow(novo_produto)

mostrar_lista()
print("produto adicionado")

#excluir 
dados = []

with open('listaprodutos.csv', 'r', newline='', encoding='utf-8') as arquivo:   #encoding='utf-8' serve para aceitar palavras com acento
    csv_reader = csv.reader(arquivo, delimiter=';') 

    for linha in csv_reader: 
        #remove apenas o registro com valor 49.9   
        if len(linha) >= 3 and linha[0] == "fone" and linha [2] == "49.9":
            continue
        dados.append(linha)         #adiciona os dados na lista

with open('listaprodutos.csv', 'w', newline='', encoding='utf-8') as arquivo:
     csv_writer = csv.writer(arquivo, delimiter=';')    
     csv_writer.writerows(dados)    #sobrescreve o valor do arquivo

mostrar_lista()
print("Produto excluido!")