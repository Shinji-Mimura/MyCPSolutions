def valid_parentheses(string):
    right = 0
    for c in string:
        if right == 0 and c == ")":
            return False
        else:
            if c == ")":
                right += 1
            elif c == "(":
                right -= 1
            else:
                continue            
    
    if right == 0:
        return True
    else:
        return False
