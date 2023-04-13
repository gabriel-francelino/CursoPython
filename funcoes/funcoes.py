# Em Python, existem diversos tipos de funções, cada uma com um propósito diferente. Abaixo, listo alguns dos tipos mais comuns:

# Funções que recebem argumentos posicionais: 
def soma(a, b):
    resultado = a + b
    return resultado

x = 2
y = 3
z = soma(x, y)
print(z)  # Saída: 5

# Funções que recebem argumentos nomeados:
def exibir_informacoes(nome, idade):
    print("Nome:", nome)
    print("Idade:", idade)

exibir_informacoes(idade=30, nome="João")  # Saída: Nome: João, Idade: 30

# Funções com argumentos padrão: 
def exibir_informacoes(nome, idade=18):
    print("Nome:", nome)
    print("Idade:", idade)

exibir_informacoes("Maria")  # Saída: Nome: Maria, Idade: 18
exibir_informacoes("João", 30)  # Saída: Nome: João, Idade: 30

# Funções que retornam valores múltiplos: 
def calcular(a, b):
    soma = a + b
    diferenca = a - b
    produto = a * b
    quociente = a / b
    return soma, diferenca, produto, quociente

x = 10
y = 2
resultado = calcular(x, y)
print(resultado)  # Saída: (12, 8, 20, 5.0)

# Funções lambda: 
# são funções anônimas e de uma única expressão que podem ser definidas em uma linha. 
dobro = lambda x: x * 2
x = 5
print(dobro(x))  # Saída: 10


