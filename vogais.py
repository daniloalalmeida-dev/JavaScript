#Escreva a função vogal que recebe um único caractere como parâmetro e
##devolve True se ele for uma vogal e False se for uma consoante.

# Note que
## vogal("a") deve devolver True
### vogal("b") deve devolver False
#### vogal("E") deve devolver True
##### Os valores True e False devolvidos devem ser do tipo bool (booleanos)
#### Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser
### um texto, ou seja, precisa estar entre aspas.

def vogal(z):
    if not isinstance(z, str) or len(z) != 1:
        return False

    vogais = ["a", "e", "i", "o", "u"]
    return z.lower() in vogais

#--------------TESTES------------------------

print("vogal(a)", vogal("a"))
print("vogal(b)", vogal("b"))
print("vogal(E)", vogal("E"))
    
