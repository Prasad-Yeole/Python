'''
Function Name    :  main()
Description      :  Demonstration Of Creating Array In Python  
Function Author  :  Prasad Yeole
Input            :  Int
Output           :  Int

'''


from array import*

def main():

    arr = array('i', [11,21,51,101,111,121]) # i is the type id of the dtype
    print(type(arr))

    print(len(arr))

    print(arr)

    for i in range(len(arr)):
        print(arr[i])

    for no in arr: # look like for each loop in java
        print(no)

    iCnt = 0
    while iCnt < len(arr):
        print(arr[iCnt])
        iCnt += 1

if __name__ == "__main__":
    main()

