# Estrutura for:

# Usada para iterar sobre uma sequência de valores e executar um bloco de código para cada valor na sequência.
# A variável definida no for é definida para cada valor na sequência.
# O bloco de código dentro do for é executado uma vez para cada valor na sequência.
for i in range(1, 6):
    print(i)

# Também é possível iterar diretamente sobre listas, strings e outros tipos de sequência:
lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(numero)

frase = "Python é uma linguagem de programação"
for letra in frase:
    print(letra)
