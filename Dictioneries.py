# Python Program To Show The Usage Of For Loop To Retrieve Elements Of Dictionaries

'''
Function Name    :  For Loop To Retrieve Elements Of Dictionaries.
Function Author  :  Prasad Yeole
Input            :  String
Output           :  String
'''

colors = {'r': "Red", 'g': "Green", 'b': "Blue", 'w': "White"}

# Dsplay Only Keys

for k in colors:
    print(k)
    
# Pass Keys To Dicttionary And Display The Values

for k in colors:
    print (colors[k])
    
# items() Method Returns Key And Values Pair Into k, v

for k, v in colors.items():
    print('key = {} value = {} '.format(k, v)) 
    