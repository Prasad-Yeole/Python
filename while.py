'''
Description      :  Use Of while With if, elif, else Statement
Function Author  :  Prasad Yeole
Input            :  Int
Output           :  Int
'''


num = 25
running = True

while running:

	value = int(input("Enter an interger : "))

	if num == value :
		print ('Congratulations, You Guessed It.')
		running = False

	elif num > value :
		print("No, It is a littel higher than that")

	else :
		print("No, It is a littel lower than that")

else:
	print("The while loop is over")

print("Done");