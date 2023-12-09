import math 

def binary_search(arr, key):

    left = 0 
    right = len(arr) 
    mid = 0 

    while (left <= right):
        mid = math.floor(((left+right)/2)) 
        if arr[mid] == key:
            return mid 
        elif key > arr[mid]:
            left = mid + 1 
        else:
            right = mid - 1 

    return -1 

testcases = [[[1,2,3,4,5], 3, 2], 
             [[5,10,15,25], 22, -1], 
             [[1,2,4,10,15,55],1,0],
               [[1,2,4,10,15,55],55,5], 
               [[1,2,4,10,15,55],15,4]] 

def assert_all(testcases):
    for testcase in testcases: 
        arr, key, expected = testcase
        assert binary_search(arr, key) == expected, str(testcase) + " failed!"

assert_all(testcases)