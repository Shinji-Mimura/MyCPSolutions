#!/bin/python3

import math
import os
import random
import re
import sys

def changes_matrix_sum(s,mg):
    aux = []
    for i in range(3):
        for j in range(3):
            if s[i][j] != mg[i][j]:
                aux2 = abs(s[i][j] - mg[i][j])
                aux.append(aux2)
    
    return sum(aux)
                
# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    
    ## All N=3 Possibilities of magic squares
    mg1 = [[8,1,6],[3,5,7],[4,9,2]]
    mg2 = [[6,1,8],[7,5,3],[2,9,4]]
    
    mg3 = [[4,9,2],[3,5,7],[8,1,6]]
    mg4 = [[2,9,4],[7,5,3],[6,1,8]]
    
    mg5 = [[8,3,4],[1,5,9],[6,7,2]]
    mg6 = [[4,3,8],[9,5,1],[2,7,6]]
    
    mg7 = [[6,7,2],[1,5,9],[8,3,4]]
    mg8 = [[2,7,6],[9,5,1],[4,3,8]]
    
    is_magic = True
    
    n = len(s)
    magic_constant = (n*(n**2 + 1)) // 2 
    
    for i in s: #sum of rows
        aux = sum(i)
        if aux != magic_constant:
            is_magic = False
    
    counter = 0
    for j in range(n): #sum of columns
        for i in range(n):
            counter += s[i][j]
            
        if counter != magic_constant:
            is_magic = False
            break
        else:
            counter = 0
    
    counter2 = 0
    for i, j in zip(range(n), range(n)): #sum of right diagonal
        counter2 += s[i][j]
    
    if counter2 != magic_constant:
        is_magic = False
        
    counter3 = 0
    j = n-1
    for i in range(n): #sum of left diagonal
        counter3 += s[i][j-i]
        
    if counter3 != magic_constant:
        is_magic = False
        
        
    if is_magic:
        return 0
    else:  
        listaaux = []
        
        listaaux.append(changes_matrix_sum(s,mg1))
        listaaux.append(changes_matrix_sum(s,mg2))
        listaaux.append(changes_matrix_sum(s,mg3))
        listaaux.append(changes_matrix_sum(s,mg4))
        listaaux.append(changes_matrix_sum(s,mg5))
        listaaux.append(changes_matrix_sum(s,mg6))
        listaaux.append(changes_matrix_sum(s,mg7))
        listaaux.append(changes_matrix_sum(s,mg8))
        
        return min(listaaux)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()


