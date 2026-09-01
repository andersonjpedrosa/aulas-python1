# Função - void
def saudacao():
    print("Olá, tudo bem?")

# Acessando a função
saudacao()

# Função com parâmetro
def saudacao(nome):
    print("Olá,", nome)

# Acessando a função
saudacao("João")

# Função de retorno
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)

# Exemplo de tratamento de erro
try:
    numero = int(input("Digite um número: "))
    print(numero)
except:
    print("Você digitou algo inválido!")

# Try e Except usando ELse e Finally juntos
try:
    numero = float(input("Digite um NOVO número: "))
except ValueError:
    print("Erro: entrada inválida")
else:
    print("Você digitou:", numero)
finally:
    print("programa finalizado")

# Exemplo de função com try e except
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero"

print(dividir(10, 2))
print(dividir(23, 0))

# Entrada do usuário
a = float(input("Digite o 1º numero: "))
b = float(input("Digite o 2º numero: "))
print(dividir(a, b))

# Loop com try e except
while True:
    try:
        n = int(input("Digite um número: "))
        print(n)
        break
    except ValueError:
        if input("Tentar novamente? (s/n): ").lower() != "s":
            break