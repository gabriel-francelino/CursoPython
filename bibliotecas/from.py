# from nome_da_biblioteca import nome_da_funcao: essa forma permite importar uma 
# função específica de uma biblioteca, sem precisar usar o prefixo do nome da biblioteca.
from math import sqrt

x = sqrt(25)
print(x) # Saída: 5.0

# from nome_da_biblioteca import *: essa forma importa todas as funções e classes de uma biblioteca, sem precisar usar o prefixo do nome da biblioteca. 
# É uma forma mais concisa, mas pode ser perigosa, pois pode haver conflitos de nomes com outras funções ou classes do seu programa.
from math import *

x = sqrt(25)
y = ceil(3.7)
print(x, y) # Saída: 5.0 4
