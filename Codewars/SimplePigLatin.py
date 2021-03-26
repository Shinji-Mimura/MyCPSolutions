
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.


def pig_it(text):
    text = text.split(" ")
    result = ""
    for i in range(len(text)):
        if text[i] != "?" and text[i] != "!":
            text[i] = text[i][1:] + text[i][0] + "ay"
            
    for i in text:
        result += i + " "        
        
    return result[:-1]
