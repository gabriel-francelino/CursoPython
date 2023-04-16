# Também é possível usar um apelido (alias) para uma biblioteca ou função importada, usando a palavra-chave as. 
# Isso é útil para evitar conflitos de nome ou para tornar o código mais legível. 
import math as m

x = m.sqrt(25)
print(x)
# Saída: 5.0

from math import sqrt as raiz_quadrada

x = raiz_quadrada(25)
print(x)
# Saída: 5.0


