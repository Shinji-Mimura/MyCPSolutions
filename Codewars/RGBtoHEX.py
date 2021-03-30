def rgb(r, g, b):
      
    if r > 10 and r <= 255:
        a1 = (hex(r).lstrip("0x").rstrip("L"))
        
    if g > 10 and g <= 255:
        a2 = (hex(g).lstrip("0x").rstrip("L"))        
        
    if b > 10 and b <= 255:
        a3 = (hex(b).lstrip("0x").rstrip("L"))   
        
    if r >= 0 and r <= 9:
        a1 = "0" + str(r)
        
    if g >=0 and g <= 9:
        a2 = "0" + str(g)        
        
    if b >=0 and b <= 9:
        a3 = "0" + str(b)
        
    if r < 0:
        a1 = "00"
    if g < 0:
        a2 = "00"
    if b < 0:
        a3 = "00"
        
    if r > 255:
        a1 = "FF"
    if g > 255:
        a2 = "FF"    
    if b > 255:
        a3 = "FF"
             
    result = a1+a2+a3
    return result.upper()
