#Escreva um programa que receba um número inteiro na entrada,
#calcule e imprima a soma dos dígitos deste número na saída

#Digite um número inteiro: 123
#6

n = int(input("Digite um número inteiro: "))

soma = 0

while n > 0:
    resto = n % 10
    n =  n // 10
    soma = soma + resto

print(soma)
