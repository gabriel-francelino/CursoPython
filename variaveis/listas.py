# As listas e conjuntos em Python são estruturas de dados diferentes e cada uma delas é mais adequada para situações específicas. Aqui estão algumas diretrizes gerais para quando usar cada uma delas:

# Use listas quando:

# Você precisa armazenar uma coleção de elementos ordenados;
# Você precisa acessar elementos individuais da coleção por posição (índice);
# Você precisa modificar os elementos da coleção.

notas = [7.5, 8.0, 6.5, 9.0]
print(notas[0])   # Saída: 7.5
notas.append(8.5)
print(notas)   # Saída: [7.5, 8.0, 6.5, 9.0, 8.5]
