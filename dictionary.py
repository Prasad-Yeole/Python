'''
Function Name    :  main()
Description      :  Demonstration of dictionary  
Function Author  :  Prasad yeole
Input            :  Int
Output           :  Int

'''

def main():

	Batches = {"PPA" : 10000, "LB" : 13000, "ANGULAR" : 17000, "MUTLIOS" : 15000}

	print(len(Batches))
	print(type(Batches))

	print(Batches)

	print(Batches["PPA"])

if __name__ == '__main__':
	main()