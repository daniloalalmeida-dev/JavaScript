#Exercício 2: Soma de matrizes

#Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que
 #represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.

#Exemplos:

#m1 = [[1, 2, 3], [4, 5, 6]]

#m2 = [[2, 3, 4], [5, 6, 7]]

#soma_matrizes(m1, m2) => [[3, 5, 7], [9, 11, 13]]

# ======================================================

#m1 = [[1], [2], [3]]

#m2 = [[2, 3, 4], [5, 6, 7]]

#soma_matrizes(m1, m2) => False

# ======================================================

def soma_matrizes(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    else:
        matriz_soma = []
        count_lines = len(m1)
        count_columns = len(m1[0])
        for i in range(count_lines):
            matriz_soma.append([])
            for j in range(count_columns):
                soma = m1[i][j] + m2[i][j]
                matriz_soma[i].append(soma)
        return matriz_soma
