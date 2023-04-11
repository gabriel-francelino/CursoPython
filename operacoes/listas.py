# Operações com listas:

# + (concatenação)
# * (repetição)
# [] (indexação)
# [:] (fatiamento)
# len() (tamanho)
# .append() (adicionar um elemento ao final)
# .insert() (inserir um elemento em uma posição específica)
# .remove() (remover o primeiro elemento com um valor específico)
# .pop() (remover e retornar o último elemento)
# .sort() (ordenar os elementos em ordem crescente)
# .reverse() (inverter a ordem dos elementos)

lista = [1, 2, 3, 4, 5]
lista.append(6)
print(lista)  # Saída: [1, 2, 3, 4, 5, 6]

lista.insert(3, 7)
print(lista)  # Saída: [1, 2, 3, 7, 4, 5, 6]

lista.remove(4)
print(lista)  # Saída: [1, 2, 3, 7, 5, 6]

lista.pop()
print(lista)  # Saída: [1, 2, 3, 7, 5]

lista.reverse()
print(lista)  # Saída: [5, 7, 3, 2, 1]

lista.sort()
print(lista)  # Saída: [1, 2, 3, 5, 7]
