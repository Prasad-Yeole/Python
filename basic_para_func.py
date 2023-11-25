'''
Description      :  Use Of Function Parameters
Function Author  :  Prasad Yeole
Input            :  Int
Output           :  Int
'''

def printMax(No1, No2):

	if No1 > No2:
		print(f"{No1} is greater than {No2}")
	elif No2 > No1 :
		print(f"{No2} is greater than {No1}")
	else :
		print("{} and {} are equal".format(No1, No2))

  # directly pass literal values

printMax(3, 4)
printMax(5,4)

  # pass variable as argumnets 

x = 5
y = 5

printMax(x,y)