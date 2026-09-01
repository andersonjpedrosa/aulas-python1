# calculos

# input: serve para escrever algo
# int: converte para núm inteiro
# float: converte para núm decimal
# print: imprime na tela

'''
num1 = input("informe o primeiro número: ")
num2 = input("informe o segundo número: ")

soma = int(num1) + int(num2)
subtracao = int(num1) - int(num2)
divisao = int(num1) / int(num2)
moduloresto = int(num1) % int(num2)     # resto da divisão (se quando divide um num pelo utro algo sobra na divisão)
multiplicacao = int(num1) * int(num2)
potenciacao = int(num1) ** int(num2)    # elevado a potencia ex.: 10² ou seja 10x10

print("O total da soma é:", soma)
print("O total da subtração é:", subtracao)
print("O total da divisão é:", divisao)
print("O total do modulo resto é:", moduloresto)
print("O total da multiplicação é:", multiplicacao)
print("O total da potenciação é:", potenciacao)

# type: retorna o tipo da variável

print(type(num1))
print(type(soma))
print(type(divisao))

# calcular área
lado1 = input("Informe o primeiro lado: ")
lado2 = input("Informe o segundo lado: ")

area = float(lado1) * float(lado2)

print("A area do quadrado é: {}" .format(area))
print("A area do quadrado é:", area)
'''

# len = retorna a quantidade de caracteres de uma variavel incluindo espaços vazios
# upper = transforma um texto em maiusculo
# lower = transforma um texto em minusculo
# capitalize = somente a primeira letra em maiusculo

nomecompleto = input("Informe o seu nome completo: ")

print("1. Quantidade de caracteres:", len(nomecompleto))
print("2. Nome em Maiusculo:", nomecompleto.upper())
print("3. Nome em Minusculo:", nomecompleto.lower())
print("4. Primeira letra em Maiusculo:", nomecompleto.capitalize())
