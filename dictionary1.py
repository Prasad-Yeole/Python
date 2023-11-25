'''
Function Name    :  main()
Description      :  Demonstration of dictionary  
Function Author  :  Prasad yeole
Input            :  Int
Output           :  Int

'''

def main():

	Batches = {"PPA" : 10000, "LB" : 13000, "ANGULAR" : 17000, "MUTLIOS" : 15000}

	for value in Batches.keys():
		print(value,end =" ")
	print();

	print("------------------------------------------------------------------------------")

	for value in Batches.keys():
		print(value, Batches[value])

	print("------------------------------------------------------------------------------")
	

	for i,j in Batches.items():
		print(i,j)

if __name__ == '__main__':
	main()