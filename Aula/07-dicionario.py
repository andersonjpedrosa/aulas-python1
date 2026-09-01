pessoa = {
    "nome": "Ana",
    "idade": 30
}

print(pessoa)
print(pessoa["nome"])

# alerando valores
pessoa["idade"] = 31
print(pessoa)

# adicionando dados
pessoa["cidade"] = "São Paulo"
print(pessoa)

pessoa["estado"] = "SP"
print(pessoa)

# removendo dados
del pessoa["idade"]
print(pessoa)

pessoa["estado"] = None
print(pessoa)

# dicionario com mais de um dado
pessoas_novas = {
    1: {
        "nome": "Vania",
        "idade": 50
    },
    2: {
        "nome": "Carlos",
        "idade": 35
    }
}
print(pessoas_novas)

# deletando um dado de um dicionário com muitos dados
# del pessoas_novas[2]
print(pessoas_novas)

# ver chaves
print(pessoas_novas.keys())
print(pessoa.keys())

# ver valores
print(pessoas_novas.values())
print(pessoa.values())

# novo dicionario
paes = {
    "nome1":"Brioche",
    "tam1":20,
    "nome2": "Frances",
    "tam2":15
}
print(paes)
print(paes.keys())
print(paes.values())

# ver chave e valor
print(paes.items())
print("nome1" in paes)
print("nome3" in paes)

# usando get
print(paes.get("nome1"))

# percorrer
for chave, valor in paes.items():
    print(chave, ":", valor)


'''
bebidas = {
    1: {
        "nome": "Coca-Cola",
        "volume": 350
    },
    2: {
        "nome": "Itaipava",
        "volume": 500
    }
}
print(bebidas)
print(bebidas.keys())
print(bebidas.values())
print(bebidas.items())
'''
