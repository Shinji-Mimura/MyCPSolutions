def sublists(arr):
    sublist = [[]]
    
    for i in range(len(arr) + 1):
        for j in range(i+1, len(arr)+1):
            sli = arr[i:j]
            sublist.append(sli)
            
    return sublist                    

def max_sequence(arr):
    
    count_positivo = 0
    for i in arr:
        if i > 0:
            count_positivo += 1
    
    if count_positivo == len(arr):
        return sum(arr)
    
    elif not arr:
        return 0
    
    else:
        sublistas = sublists(arr)
        maior = 0
        for sub in sublistas:
            if sum(sub) > maior:
                maior = sum(sub)
        
        return maior
    
