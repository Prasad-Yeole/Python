'''
Description      :  Input In Function By .format Method
Function Author  :  Prasad Yeole
Input            :  Int
Output           :  Int
'''

# defination of function, use of .format method

def Addition(no1, no2):
	ans = no1 + no2;
	return ans

def main():
	print("Enter the first number : ")
	value1 = int(input())

	value2 = int(input("Enter the Second Value"))

	ret = Addition(value1, value2)
	print(f"Addition of {value1} and {value2} is {ret}")

	# Another way to use format string
	# print("Addition of {} and {} is {} ".format(value1, value2, ret)) 

if __name__ == '__main__':
	main()