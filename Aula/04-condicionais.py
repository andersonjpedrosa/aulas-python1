numero = int(input('Informe um número: '))

resultado = int(numero % 2)

print('Se o resultado for 0 é par e se for 1 é impar, o resultado é:', resultado)
input('Digite ENTER para continuar')

# if é usado para tomada de decisão
if resultado == 0:
    resultado = 'O número é par'
else:
    resultado = 'O número é impar'
print(resultado)

input('Digite ENTER para continuar')

# limpar o terminal
import subprocess
import os

comando = "cls" if os.name == "nt" else "clear"
subprocess.run(comando, shell=True)

# Entrada da nota
nota = float(input("Digite a nota do estudante: "))

# Verificação da situação
if nota >=7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")



