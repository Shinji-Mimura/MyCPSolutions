
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).



def to_camel_case(text):
    
    string_final = ''

    if len(text) == 0:
        return ""
    
    else:
        text = text.replace("_","-")
        lista = text.split("-")
        if lista[0][0] != lista[0][0].upper():
            string_final += lista[0]
            for i in range(1,len(lista)):
                 string_final += lista[i].capitalize()
                
        else:
            for i in range(len(lista)):
                string_final += lista[i].capitalize()
                            
    return string_final
