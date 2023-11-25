'''
Description      :  Performing New Variations In Functions  
Function Author  :  Prasad Yeole
Input            :  Str
Output           :  Str
'''

print("Demonstration Of Advanced Functions ")

# 1 : Function Which Accepts Nothing And Returns Nothing

def Function1():
	print("Inside Function1.")

# 2 : Function Which Accepts Parameters And Returns Nothing

def Function2(iNo1):
	print("Inside Function2.")
	print("Accepted value is : ",iNo1)

# 3 : Function which Aceepts Parameter Returns Value

def Function3(iNo1):
	print("Inside Function3.")
	print("Accepted value is : ",iNo1)
	return iNo1 + 1;

# 4 : Function which Aceepts value And Returns multiple Values

def Function4(iNo1,iNo2):
	print("Inside Function4")
	add = iNo1 + iNo2
	sub = iNo1 - iNo2
	return add, sub

# 5 : Function which Calls Another Function which Is Defined Outside It

def Function5():
	print("Inside Function5")
	Function1();

# 6 : Function Which Contain Another Nested Function defined In It

def Function6():
	print("Inside Function6")

	def InnerFun():
		print("Inside InnerFun")
	InnerFun()

# Main Function

def main():

	No = 9;

	Function1()

	Function2(No)

	ret = Function3(No)
	print("Return value is : ",ret);

	ret1, ret2 = Function4(10, 4)
	print("Addition is : ",ret1);
	print("Sub is subtraction : ",ret2);

	Function5()

	Function6()

if __name__ == '__main__':
	main()