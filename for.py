'''
Description      :  Basic For-Loop 
Function Author  :  Prasad Yeole
Input            :  Int
Output           :  Int
'''

def Addition(*no):

	sum = 0;

	for number in no :
		sum += number
	
	return sum;

def main() :
	ret = Addition(10,20,30,40)
	print(f"Addition is : {ret}")

	ret = Addition(50,40)
	print(f"Addition is : {ret}")

if __name__ == '__main__':
	main()