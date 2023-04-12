# A função input() é usada para ler a entrada do usuário a partir do teclado.
nome = input("Qual é o seu nome? ")
print("Olá, " + nome + "! Bem-vindo ao Python!")

# A função print() é usada para exibir uma mensagem na tela.
print("Olá, mundo!")
print("O resultado é:", 42)
print("2 + 2 =", 2 + 2)

# Também é possível formatar a saída usando as strings formatadas.
nome = "João"
idade = 30
print(f"{nome} tem {idade} anos.")

# Ao ler números, é importante converter a entrada de string para o tipo numérico apropriado. 
# Em Python, existem três tipos numéricos principais: int, float e complex.
# Ler um número inteiro
num_inteiro = int(input("Digite um número inteiro: "))
print("Você digitou o número inteiro:", num_inteiro)

# Ler um número real (float)
num_real = float(input("Digite um número real: "))
print("Você digitou o número real:", num_real)

# Ler um número complexo
num_complexo = complex(input("Digite um número complexo (no formato a+bj): "))
print("Você digitou o número complexo:", num_complexo)

# Além disso, também é possível ler vários valores em uma única linha de entrada, 
# separando-os com um espaço ou outro caractere de separação.
# Ler dois números inteiros separados por espaço
x, y = input("Digite dois números inteiros separados por espaço: ").split()
x = int(x)
y = int(y)
print("Você digitou os números inteiros:", x, "e", y)

# Ler uma lista de números separados por vírgula
numeros = input("Digite uma lista de números separados por vírgula: ").split(",")
numeros = [float(x) for x in numeros]
print("Você digitou a lista de números:", numeros)

# A função split() é usada para separar a entrada do usuário em uma lista de strings, 
# que é então convertida para uma lista de números usando a compreensão de lista.