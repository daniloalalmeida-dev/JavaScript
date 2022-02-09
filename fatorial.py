n = int(input("Digite um número n: "))
if (n<0):
        print("Valor inválido! Fim do programa.")
else:
        fat = 1
        while (n>1):
                fat = fat * n
                n = n - 1
print(fat)        
