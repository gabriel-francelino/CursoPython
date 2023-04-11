# Use conjuntos quando:

# Você precisa armazenar uma coleção de elementos únicos e não ordenados;
# Você precisa verificar rapidamente se um elemento está na coleção;
# Você precisa realizar operações de conjunto, como união, interseção ou diferença.

numeros = {1, 2, 3, 4, 5}
if 3 in numeros:
    print("3 está na coleção de números")
# Saída: "3 está na coleção de números"

letras1 = {"a", "b", "c", "d"}
letras2 = {"c", "d", "e", "f"}
uniao = letras1.union(letras2)
print(uniao)   # Saída: {'c', 'f', 'a', 'e', 'b', 'd'}
