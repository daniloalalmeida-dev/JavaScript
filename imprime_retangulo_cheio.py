# Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo,
# respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

# Por exemplo:

# digite a largura: 10
## digite a altura: 3
##########
##########
##########
    
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
caractere = "#"


def retângulo(largura, altura, caractere):

    linha = caractere * largura

    for i in range(altura):
        print(linha)

retângulo(caractere, altura, largura)
