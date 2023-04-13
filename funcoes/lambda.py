# Em Python, as funções lambda são funções anônimas, ou seja, não possuem um nome definido. 
# Elas são criadas usando a palavra-chave lambda seguida pelos argumentos da função separados por vírgulas, 
# seguidos por dois pontos e a expressão que será retornada pela função.

# A principal vantagem das funções lambda é que elas permitem criar funções simples 
# e de uma única expressão sem a necessidade de definir uma função com um nome específico. 
# Elas são frequentemente usadas em conjunto com outras funções como 'map()', 'filter()' e 'reduce()'.
# Criando uma função lambda para somar dois números
soma = lambda x, y: x + y

# Usando a função lambda
print(soma(2, 3))  # Saída: 5

# Usando a função lambda com map()
numeros = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x * 2, numeros))
print(dobro)  # Saída: [2, 4, 6, 8, 10]

# Usando a função lambda com filter()
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4]
