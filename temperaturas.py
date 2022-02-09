#Temperaturas
#Consultar temperaturas

#Quebrar o problema em problemas menores

#Temperatura mínima e Máxima

def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ", mínima(temperaturas), "c.")
    print("A maior temperatura do mês foi: ", máxima(temperaturas), "c.")

def mínima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def máxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

temperaturas = [20, 18, 24, 45, 60]

MinMax(temperaturas)
