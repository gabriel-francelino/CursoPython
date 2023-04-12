# if: Essa é a estrutura condicional mais básica em Python. Ela é usada para executar um bloco de código se uma condição for verdadeira.

# if-else: Essa estrutura condicional é usada para executar um bloco de código se a condição for verdadeira e outro bloco de código se a condição for falsa.

# if-elif-else: Essa estrutura condicional é usada quando há mais de duas condições a serem avaliadas. Ela permite avaliar várias condições em sequência e executar um bloco de código correspondente à primeira condição verdadeira encontrada. Se nenhuma condição for verdadeira, o bloco de código associado ao else é executado.

# nested if: Esse tipo de estrutura condicional é usado quando uma condição precisa ser avaliada dentro de outra condição. É possível ter várias condições aninhadas dessa forma.

# Operador ternário: Esse é um tipo de estrutura condicional compacta que pode ser usada para avaliar uma expressão condicional em uma única linha de código. A sintaxe é a seguinte: valor_verdadeiro if condição else valor_falso.

idade = 20
if idade < 18:
    print("Você é menor de idade")
else:
    print("Você é maior de idade")

idade = 15
maioridade = "Você é maior de idade" if idade >= 18 else "Você é menor de idade"
print(maioridade)

idade = 25
if idade < 18:
    print("Você é menor de idade")
elif idade < 25:
    print("Você é jovem")
elif idade < 60:
    print("Você é adulto")
else:
    print("Você é idoso")

a = 10
b = 20
if a > 5:
    if b > 10:
        print("a é maior que 5 e b é maior que 10")

