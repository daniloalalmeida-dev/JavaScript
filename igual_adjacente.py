#Exercício 2 - Desafio do vídeo "Repetição com while"
#Escreva um programa que receba um número inteiro na entrada e verifique se
#o número recebido possui ao menos um dígito com um dígito adjacente igual a ele.
#Caso exista, imprima "sim"; se não existir, imprima "não".

#Exemplos:

#Digite um número inteiro: 123
#não

#Digite um número inteiro: 3556
#sim

n = int(input("Digite um número inteiro: "))

test = 0
x = 0

while n > 1:        
    resto = n%10 #123/10 == 3
    n = n // 10 #123 // 10 == 12
    x = n % 10  # 12 / 10 == 2
    y = n // 10 # 12 // 10 == 1
    
if y == x or y == n or resto == x or resto == y:
    print("sim")
else:
    print("não")
    
