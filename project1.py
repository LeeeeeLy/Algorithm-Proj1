import random
import sys
from time import time
from datetime import timedelta
sys.setrecursionlimit(1000000000)

#generates n random integers
def randnumg(n):
    """
    Generate array of random data
    - input: length of the data
    - output：array of random data
    """
    lst = []
    #limit the range to prevent memory error when data size is 1E9
    if n <= 100000:
        rangee = n*10
    else:
        rangee = 1000000
    for i in range(n):
        lst.append(random.randint(1,rangee))
    return lst
    
    
#generates 3 different types of data
def caseg(n,types):
    """
    Generate 3 different types of data
    - input: length of the data, desired type 
    - output：array of desired data
    """
    if types == 's':#Increasing data that is already sorted (1to n) 
        case1 = [i for i in range(n)]
        return case1
    elif types == 'c':#Array of all 0’s (constant data)
        case2 = [0]*n
        return case2
    elif types == 'r':#Array of random data 
        case3 = randnumg(n)
        return case3
    else:
        print('Wrong input for data type')



def selectionsort(case):
    """
    Selection sort
    - input: array
    - output：sorted array
    """
    n = len(case)
    for i in range(0,n):
        #find the next min
        
        for j in range(i+1, n):
            if case[j] < case[i]:    
                #insert min to the right position
                temp = case[i]
                case[i] = case[j]
                case[j] = temp
                
    return case

def insertionsort(case):
    """
    Insertion sort
    - input: array
    - output：sorted array
    """
    for i in range(1,len(case)):
        pos = case[i]
  
        # Move every elements after ith element and greater than ith element 
        j = i-1
        while pos < case[j] and j >=0:
            case[j+1] = case[j]
            j = j - 1
        case[j+1] = pos
    return case    


def midof3(case,left,right):
    """
    median-of-three strategy
    - input: array, left and right index
    - output：index of the midian value
    """
    mid = (left + right)//2
    left_v = case[left]
    right_v = case[right-1]
    mid_v = case[mid]
    
    if left_v <= mid_v <= right_v:
        return mid
    elif right_v <= mid_v <= left_v:
        return mid
    elif mid_v <= left_v <= right_v:
        return left
    elif right_v <= left_v <= mid_v:
        return left
    else:
        return right-1
    
def partition(case,left,right):
    """
    Partition for quicksort
    - input: array, left and right index
    - output：index
    """
    #get the pivot position
    pivot_pos = midof3(case,left,right)
    pivot = case[pivot_pos]
    case[pivot_pos] = case[left]
    case[left] = pivot
    
    i = left + 1
    for j in range(left + 1, right):
        
        if case[j] < pivot:
            temp = case[i]
            case[i] = case[j]
            case[j] = temp
            i = i + 1
            
    temp = case[left]
    case[left] = case[i-1]
    case[i-1] = temp
    return i - 1  

def quicksort(case,left,right):
    """
    Quicksort
    - input: array, left and right index
    - output：sorted array
    """
    if left < right:
        pivot_pos = partition(case,left,right)
        #recursive calls
        quicksort(case,left,pivot_pos)
        quicksort(case,pivot_pos+1,right)    
    return case

def checksorted(lst):
    """
    Check if an array is correctly sorted
    - input: array
    - output：0 - sorted, 1 - not sorted
    """
    boolean = 0
    i = 1
    while i < len(lst):
        if(lst[i] < lst[i - 1]):
            flag = 1
        i = i + 1
    return boolean    
        

if __name__ == "__main__":
    if(len(sys.argv) == 4):
        n = int(sys.argv[2])
        cases = caseg(n,sys.argv[3])
        if sys.argv[3] == 'c':
            ty = 'constant'
        elif sys.argv[3] == 'r':
            ty = 'random'
        elif sys.argv[3] == 's':
            ty = 'sorted'
        else:
            ty = 'not defined'
        if sys.argv[1] == 'q':
            stime = time()  
            lstq = quicksort(cases,0, len(cases))
            etime = time()
            etime = etime - stime
            print('Sorting',n,'numbers of',ty,'data with quicksort takes:')
            print("{:0>8}".format(str(timedelta(seconds=etime))))
            if (not checksorted(lstq)):
                print ("Data correctly sorted after running <quicksort>.")
            else :
                print ("ata incorrectly sorted after running <quicksort>.")
        elif sys.argv[1] == 'i':
            stime = time()
            lsti = insertionsort(cases)
            etime = time()
            etime = etime - stime
            print('Sorting',n,'numbers of',ty,'data with insertionsort takes:')
            print("{:0>8}".format(str(timedelta(seconds=etime))))
            if (not checksorted(lsti)):
                print ("Data correctly sorted after running <insertionsort>.")
            else :
                print ("ata incorrectly sorted after running <insertionsort>.")
        elif sys.argv[1] == 's':
            stime = time()
            lsts = selectionsort(cases)
            etime = time()
            etime = etime - stime
            print('Sorting',n,'numbers of',ty,'data with selectionslot takes:')
            print("{:0>8}".format(str(timedelta(seconds=etime))))
            if (not checksorted(lsts)):
                print ("Data correctly sorted after running <selectionslot>.")
            else :
                print ("ata incorrectly sorted after running <selectionslot>.")
    else:
        print('Wrong input for sort method')
