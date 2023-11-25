'''
Function Name    :  main()
Description      :  variations on dictionary  
Function Author  :  Prasad yeole
Input            :  Int
Output           :  Int

'''

def main():

	Batches = {"PPA" : 10000, "LB" : 13000, "ANGULAR" : 17000, "MUTLIOS" : 15000}

	Name = input("Enter the name of batch : ")

	print(Batches.get(Name, "Batch is not present."))


if __name__ == '__main__':
	main()