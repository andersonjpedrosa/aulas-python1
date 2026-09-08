import json

# r = read - ler
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(dados)
print(dados["nome"])

#convertendo json em str (string)
texto = json.dumps(dados, indent=4, ensure_ascii=False)
print(texto)

#convertendo o str em json
pessoa_nova = '{"primeironome": "Paulinho", "idade": 39}'

dados_novo = json.loads(pessoa_nova)
print(dados_novo)

#atualizando
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

dados["idade"] = 38     #alteração
dados["rede_social"] = "@andersonjpart" #adicionando um dado novo
del dados["telefone"]   #deletando um dado

# w = write - escrever
with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print("Dado adicionado com sucesso!")
print("Telefone removido com sucesso!")
print(dados)