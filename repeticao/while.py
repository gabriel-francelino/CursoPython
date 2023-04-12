# Estrutura while:

# Usada para repetir um bloco de código enquanto uma condição for verdadeira.
# A condição é verificada no início de cada iteração.
# O bloco de código dentro do while é executado várias vezes, desde que a condição seja verdadeira.
# Se a condição for falsa, o bloco de código dentro do while é ignorado e a execução do programa continua a partir da próxima instrução após o while.
i = 1
while i <= 5:
    print(i)
    i += 1

# Em Python, não existe uma estrutura de repetição do while como em algumas outras linguagens de programação, como C e Java.
# Em vez disso, pode-se usar uma estrutura while com uma condição inicializada como True e um comando break dentro do bloco de código, 
# de modo que o loop seja executado pelo menos uma vez.
while True:
    # código a ser executado
    resposta = input("Deseja continuar? (S/N): ")
    if resposta.upper() == "N":
        break


