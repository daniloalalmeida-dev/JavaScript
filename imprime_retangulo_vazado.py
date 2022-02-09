# Refaça o exercício 1 imprimindo os retângulos sem preenchimento,
## de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

# Exemplo:

# digite a largura: 10
# digite a altura: 3
##########
#        #
##########

def retangulo(largura, altura, caractere):
    print(caractere * largura) # cabeçalho

    for i in range(altura - 2):
        espacos = (largura - 2) * ' '
        print("%s%s%s" % (caractere, espacos, caractere)) # meio

    print(caractere * largura) # rodapé

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
caractere = "#"

retangulo(largura, altura, caractere)
