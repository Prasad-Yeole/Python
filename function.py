'''
def Hello(to="World"):
	print("Hello,", to);

Hello();  	
name = input("What's your name? ");
Hello(name);
'''

# if we define the hello function after the the function call than it will rewult inn error 
# to solve this problem we can use main function by defing all the function top to down wrting logic as needed and than giving calll to the main function 
# example

def main():
	name = input("What's your name? ");
	hello(name);

def hello(to = "World"):
	print("Hello,", to);

main();
