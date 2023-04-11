# Operações com conjuntos:

# union() (união)
# intersection() (interseção)
# difference() (diferença)
# symmetric_difference() (diferença simétrica)
# issubset() (verificar se um conjunto é subconjunto de outro)
# issuperset() (verificar se um conjunto é superconjunto de outro)

conj1 = {1, 2, 3, 4, 5}
conj2 = {4, 5, 6, 7, 8}

print(conj1.union(conj2))    # Saída: {1, 2, 3, 4, 5, 6, 7, 8}
print(conj1.intersection(conj2))   # Saída: {4, 5}
print(conj1.difference(conj2))     # Saída: {1, 2, 3}
print(conj1.symmetric_difference(conj2))  # Saída: {1, 2, 3, 6, 7, 8}

conj1.add(6)
print(conj1)   # Saída: {1, 2, 3, 4, 5, 6}

conj1.remove(3)
print(conj1)   # Saída: {1, 2, 4, 5, 6}
