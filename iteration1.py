'''
Description      :  Sequence Vs Iteration Approach  
Function Author  :  Prasad Yeole
Input            :  Int
Output           :  str

'''

# sequance approach

def startS():
    print("Jay Ganesh")
    print("Jay Ganesh")
    print("Jay Ganesh")

# Iteration approach

def startI():
    icnt = 0
    while icnt < 5:
        print("Jay Ganesh")
        icnt = icnt + 1

def main():
    print("Output by sequance approach")
    startS()

    print("Output by iteration approach")
    startI()

if __name__ == "__main__":
    main()