#Um número primo é um número natural maior do que 1
#que tem apenas dois divisores positivos distintos, 1 e ele mesmo.

#Escreva um programa que receba um número inteiro positivo na entrada
#e verifique se é primo. Se o número for primo,
#imprima "primo". Caso contrário, imprima "não primo".

#Exemplos:

#Digite um número inteiro: 11

#primo

#Digite um número inteiro: 12

#não primo

n = int(input("Digite um número inteiro: "))

if n % 2 == 0 and n != 2:
    print("não primo")
else:
    print("primo")
