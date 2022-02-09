# Escreva a função soma_elementos
## que recebe como parâmetro uma lista com números inteiros
## e devolve um número inteiro correspondente à soma dos
# elementos da lista recebida.

def soma_elementos(lista):
    soma = 0
    for elem in lista:
        soma += elem
    return soma

lista = [1, 3, 6, 9, 12, 15] #len(lista) == 6

somado = soma_elementos(lista)
print(somado)
        
