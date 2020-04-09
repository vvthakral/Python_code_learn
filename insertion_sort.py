#Insertion sort in Python
#Sort the array and also check for the time complexity being O(input_size^2)
#By Vishnu Vansh Thakral

import random
import time

n1 = int(input('Enter size of first array for sorting'))
n2 = int(input('Enter size of second array for sorting'))

arr1 = random.sample(range(1,n1+1),n1)
#print(arr1)

arr2 = random.sample(range(1,n2+1),n2)
#print(arr2)

def insertion_sort(arr):
    start = time.time()
    for i in range(1,len(arr)):
        if arr[i] >= arr[i-1]:
            continue
        else:
            j = i
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
    end = time.time()
    return (arr, end-start)

arr1, time1 = insertion_sort(arr1)
#print('sorted arr1 is %s'%arr1)
print('Time taken to sort arr1 is %s'%(time1))
arr2, time2 = insertion_sort(arr2)
#print('sorted arr2 is %s'%arr2)
print('Time taken to sort arr2 is %s'%(time2))
print ('we know that time taken for insertion sort is proportional to square of array size')
print('The ratio of square of sizes is %s'%(n1**2/n2**2))
print('The ratio of time taken is  %s'%(time1/time2))