# comentário de uma linha

''' comentários em mais linhas
devem ficar entre 3 aspas simples '''

# concatenação
print('Boas vindas a aula de ' + 'Python!')

''' # interpolação
print('Olá {}' .format(input('Qual o seu nome? ')))

# tipos de dados em python - números '''

# inteiro (int)
idade = 38
print(idade)

# decimal (float)
altura = 1.75
print(altura)

''' # teste de texto com variável
peso = 70
print('peso: ',peso,'kg')

# concatenando texto e variável
kg = 69
print('peso2: ' + str(kg) + ' kg') '''

# numero complexo - quando tem texto junto com número
numero_complexo = 2 + 3j
print(numero_complexo)

# texto(str)
nome = "Anderson"
print(nome)

# booleano(bool) - só guarda os valores True ou False
ativo = True
print(ativo)

logado = False
print(logado)

# nenhum valor (NoneType)
valor = None
print(valor)

# lista (list) / mutável
frutas = ["maçã" , "banana" , "uva"]
print(frutas)

# tupla(tuple) / imutável - também é uma lista
cores = ("vermelho" , "azul" , "verde")
print(cores)

# conjunto(set) - também é mutável, usado quando tem somente números
numeros = {1, 2, 3, 4}
print(numeros)

# dicionario(dict) pares chave-valor - pode receber vários tipos de dados
pessoa = {
    "nome": "Ana",
    "idade": 30
}
print(pessoa)

''' Python não tem constantes verdadeiras,
mas usamos uma convenção para indicar que
um valor não deve ser alterado '''

''' colocamos a "variavel" em MAIUSCULA para identificar que
ela não deve ser alterada então ela vira uma constante '''

PI = 3.14159
GRAVIDADE = 9.8

print("o valor de PI é", PI , "\nO valor de Gravidade é" , GRAVIDADE)

# O comando \n pula linha dentro do texto