def mergeSort (arr):
    if(len(arr)==1):
        return arr

    middle = len(arr)//2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])

    res = []   
    i=0
    j=0

    while (i<len(left) and j<len(right)):
        if(left[i] < right[j]):
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1

    while i<len(left):
        res.append(left[i])
        i+=1

    while j<len(right):
        res.append(right[j])
        j+=1

    return res

x = [3,2,5,6,1,-1,0,10000]
x = mergeSort(x)
print(x)