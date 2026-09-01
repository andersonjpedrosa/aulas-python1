#Operadores de Comparação

a = 10
b = 5

print(a > b)  #maior que
print(a < b)  #menor que

print(a == b)  #igual
print(a != b)  #diferente

print(a >= b)   #maior ou igual
print(a <= b)   #menor ou igual

# ------------------------------------------------------

#Operadores Lógicos

numero = 10

print('Operadores Lógicos')

#No AND o resultado é TRUE se os dois lados forem TRUE
print(numero > 5 and numero < 15)

#No OR o resultado é TRUE se somente um dos lados for TRUE
print(numero < 5 or numero == 10)

#NOT pega o booleano original e nega ele TRUE vira FALSE e vice versa
print(not(numero > 5))