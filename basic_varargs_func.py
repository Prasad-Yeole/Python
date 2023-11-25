'''
Description      :  Use Of VarArgs Parameters In Function 
Function Author  :  Prasad Yeole
Input            :  Int
Output           :  Int
'''

def total(initial = 5, *numbers, **keywords): # One * Is Consider As Tuple & ** Is Consider As Dictionary
    count = initial
 
    for number in numbers:
        count += number
 
    for key in keywords:
        count += keywords[key]
    return count

print (total(4, 1, 2, 3, vegetables = 40, fruits = 100))