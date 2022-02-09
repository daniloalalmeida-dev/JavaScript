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
    for num in reversed(range(1,n+1)):
        if all(num%i!=0 for i in range(2,num)):
            return num

#----------TESTES-----------
print("maior_primo(100)", maior_primo(100))
print("maior_primo(7)", maior_primo(7))  


