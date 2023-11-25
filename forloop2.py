'''
Description      :  Use Of Forloop With Hardcoded Value
Function Author  :  Prasad Yeole
Input            :  Int
Output           :  str

'''

def display():
    print("Output of For loop")
    icnt = 0
    for icnt in range(10, 1, -2):
        print(icnt)
    else:
        print("End of For loop")

def main():
    display()

if __name__ == "__main__":
    main()


def display():
    for _ in range(10,2,-1):
        print(_)

def main():
    display()

if __name__ == '__main__':
    main()