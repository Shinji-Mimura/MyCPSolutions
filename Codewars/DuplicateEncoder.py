
# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.



def duplicate_encode(word):
    lista_singulares = []
    lista_repetidos = []
    
    blacklist = []
    
    word = word.upper()
    
    for letter in word:
        if word.count(letter) > 1 and letter not in blacklist:
            lista_repetidos.append(letter)
        if word.count(letter) < 1 and letter not in blacklist:
            lista_singulares.append(letter)
            
    
    result = ''
    
    for letter in word:
        if letter in lista_repetidos:
            result += ')'
        else:
            result += '('
            
    return result
