def bubble_sort(arr,order='a'):
    if order == 'd':
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j]<arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
    else:
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr =[int(x) for x in input("Enter the input array to sort: ").split()]
order = input('Enter d for descending else a or ascending')
print(bubble_sort(arr,order.lower()))