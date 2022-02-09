def sameShape(m1, m2):
    '''Verificação manual se duas listas têm o mesmo formato'''

    if type(m1) != type(m2):
        return False

    if type(m1) == list:
        if len(m1) != len(m2):
            return False

        for i in range(len(m1)):
            if not sameShape(m1[i], m2[i]):
                return False

    return True

def soma_matrizes(m1, m2):
    if not sameShape(m1, m2):
        return False
    else:
        # Reduz a dimensão da matriz de 2 pra 1 (i.e. transforma em lista simples)
        # para facilitar a soma
        m1 = [i for j in m1 for i in j]
        m2 = [i for j in m2 for i in j]

        # Calcula a soma item a item das duas listas
        s = [sum(t) for t in zip(m1, m2)] # <= usa `sum` em cada tupla
        #s = [i + j for i, j in zip(m1, m2)] # <== alternativa (talvez mais fácil de entender)

        # Faz a lista de soma ter 2 dimensões antes de retornar
        k = int(len(s) / 2)
        return [s[:k], s[k:]]

m1 = [[1, 2, 3],[4, 5, 6]]
m2 = [[2, 3, 4],[5, 6, 7]]
print(soma_matrizes(m1, m2))

m1 = [[1], [2], [3]]
m2 = [[2, 3, 4],[5, 6, 7]]
print(soma_matrizes(m1, m2))
