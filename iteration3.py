'''
Description      :  Display N Number Of Iteration From User With Message 
Function Author  :  Prasad Yeole
Input            :  Int
Output           :  str

'''

def startdynamic(no, message = "Jay Ganesh"):
    icnt = 0
    while icnt < no:
        print(message)
        icnt = icnt + 1

def main():
    print("enter number of iterations")
    value = int(input())
    print("enter the message")
    name = input()

    startdynamic(value, name)
    startdynamic(value)

if __name__ == "__main__":
    main()
