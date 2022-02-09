#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
#Note que
#maior_primo(100) deve devolver 97
#maior_primo(7) deve devolver 7

# Dica: escreva uma função éPrimo(k)
## e faça um laço percorrendo os números até o número dado checando
### se o número é primo ou não;
#### se for, guarde numa variável.
##### Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.

def maior_primo(n):

    primos = []
    for i in range(n):
        c = 0
        for j in range(n):
            if i%(j+1) == 0: 
                c += 1
        if c == 2:
            primos.append(i)

    return(max(primos))

#----------TESTES-----------
print("maior_primo(100)", maior_primo(101))
print("maior_primo(7)", maior_primo(8))
    


