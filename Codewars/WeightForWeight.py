def sum_numbers(string):
    count = 0
    for l in string:
        count += int(l)
    
    return count

def order_weight(string):
    
    lista_numeros = string.split(" ")
    lista_numeros = sorted(lista_numeros)
    lista_soma_numeros = []
    somador = 0
    
    for n in lista_numeros:
        for i in range(len(n)):
            somador += int(n[i])
        lista_soma_numeros.append(somador)
        somador = 0
        
    lista_soma_numeros = list(set(lista_soma_numeros))
    lista_soma_numeros.sort()

    aux = ''
    
    for n in lista_soma_numeros:
        for i in lista_numeros:
            if n == sum_numbers(i):
                aux += i + " "
                
    return aux[:-1]
