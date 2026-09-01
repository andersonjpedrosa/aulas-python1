#loop for
for i in range(1, 6):
    print(i)

frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)

print("\n") # pula linha

# loop for com continue (pula o 5)
for j in range(1, 11):
    if j == 5:
        continue
    print(j)

print("\n") # pula linha

# loop for com break (para no 4)
for m in range(1, 11):
    if m == 5:
        break
    print(m)

print("\n") # pula linha

# loop for com continue e break juntos
for n in range(1, 11):
    if n == 5:
        continue    # pula o num 5

    if n == 8:
        break       # para o loop quando chegar na posição 8

    print(n)

print("\n") # pula linha

# loop while (enquanto)
texto = ""

while texto != "sair":  # enquanto for diferente (!=) de sair
    texto = input("Digite algo (ou 'sair' para parar): ")

print("\n") # pula linha

# loop while com contator
contador = 1

while contador <= 5:
    print(contador)
    contador += 1   # incremento +1

print("\n") # pula linha

# não devemos fazer - loop infinito
while True:
    print("Este loop é infinito!")

