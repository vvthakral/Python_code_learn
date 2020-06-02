def merge_sort(arr):
    c = len(arr)//2
    if c>=1:    
        l = arr[:c]
        r = arr[c:]
        l = merge_sort(l)
        r = merge_sort(r)
    else:
        return arr
    p_l,p_r = 0,0
    arr = []
    while True:
        if p_l < len(l) and p_r < len(r):
            if l[p_l]<r[p_r]:
                arr.append(l[p_l])
                p_l+=1
            else:
                arr.append(r[p_r])
                p_r+=1
        elif p_l == len(l) and p_r<len(r):
            arr.extend(r[p_r:])
            break
        elif p_r == len(r) and p_l<len(l):
            arr.extend(l[p_l:])
            break
    return arr

a = [int(x) for x in input ('Enter the array   :').split(' ')]
merge_sorted = merge_sort(a)
print(merge_sorted)