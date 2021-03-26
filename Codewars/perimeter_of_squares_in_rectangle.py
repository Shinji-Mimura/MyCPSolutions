
# The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80



def calculateSum(n) :
    if (n <= 0):
        return 0
  
    fibo =[0] * (n+1)
    fibo[1] = 1
  
    sm = fibo[0] + fibo[1]
  

    for i in range(2,n+1) :
        fibo[i] = fibo[i-1] + fibo[i-2]
        sm = sm + fibo[i]
         
    return sm

def perimeter(n):
    
    result = 4 * calculateSum(n+1)
    return result
    
