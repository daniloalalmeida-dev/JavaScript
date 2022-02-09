#Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.
#Note que
#maximo(3,4) deve devolver 4
#maximo(0,-1) deve devolver 0

def maximo(n,k):
    if n > k:
        return(n)
    else:
        return(k)

#---------------------TESTES-------------------------
print("maximo(3, 4)", maximo(3,4))
print("maximo(0,-1)", maximo(0,-1))
