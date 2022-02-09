# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros,
## verifica se tal lista possui elementos repetidos e os remove.
## A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

# Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

def remove_repetidos(lista):
    lista_limpa = []
    for igual in lista:
        if igual not in lista_limpa:
            lista_limpa.append(igual)
    lista_limpa.sort()
    return lista_limpa

lista = [5, 7, 5, 0, 11, 14, 11, 14, 1, 0, 1, 14, 9, 8, 9] #15

lista = remove_repetidos(lista)
print(lista)


#Forma mais simples de remover repetidos, sem dor!!
                  
#lista = [5, 7, 5, 0, 11, 14, 11, 14, 1, 0, 1, 14, 9, 8, 9] #15

#remove_repetidos = list(set(lista))
#print(remove_repetidos)
