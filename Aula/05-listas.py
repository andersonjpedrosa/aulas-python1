# limpar o terminal
import subprocess
import os

comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)

# -----------------------------------------------

frutas = ["maça", "banana", "uva"]
print(frutas)

# ver um elemento da lista
print(frutas[0])

# retornando demais elementos do seu index
print(frutas[1])
print(frutas[2])

# modificando
frutas[1] = "laranja"
print(frutas)

# adicionando itens no final da lista
frutas.append("pera")
print(frutas)

# adicionando no começo da lista
frutas.insert(0, "abacaxi")
print(frutas)

# removendo itens da lista
frutas.remove("abacaxi")
print(frutas)

if "abacaxi" in frutas:
    print("abacaxi está na lista")
else:
    print("abacaxi não está na lista")


# procurando um item
indice = frutas.index("uva")
print(indice)

'''
if "uva" in frutas:
    print(f"uva está na lista na posição {indice}")
else:
    print("não tem uva na lista")

dfruta = input("digite a fruta que quer procurar: ")
if dfruta in frutas:
    indice = frutas.index(dfruta)
    print(f"{dfruta} está na lista na posição {indice}")
else:
    print(f"não tem {dfruta} na lista")

'''

# tamanho da lista
numeros = [100, 28, 4, 31]
print(len(numeros))

# ordenar
numeros.sort()
print(numeros)

frutas.sort()
print(frutas)

# inverter
numeros.reverse()
frutas.reverse()

print(numeros)
print(frutas)

# verificar se existe
print(2 in numeros)

# adicionando varios elementos
numeros = [10, 20, 30] + numeros
print(numeros)

frutas = ["morango", "melancia"] + frutas
print(frutas)

# percorrer uma lista com for
for n in numeros:
    print(n)

print(type(n))
print(type(numeros))
print(type(frutas))