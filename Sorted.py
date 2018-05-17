# SelectSort
def   findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1 , len(arr) ) :
        if arr[i]<smallest :
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def  SelectSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest)) 
    return newArr



# ------------------------------------------------------
# mergeSort

def   mergeSort(arr):
    mid = len(arr)//2
    lft , rgt = arr[:mid], arr[mid:]
    if len(lft)>1 : lft = mergeSort(lft)
    if len(rgt)>1 : rgt = mergeSort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] > rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    
    return (lft or rgt) + res



# ------------------------------------------------------
# quickSort
def  quickSort(arr):
    if len(arr) < 2 :
        return arr
    else:
        pivot = arr[0]
        less = [ i for i in arr[1:] if i<=pivot ]
        greater = [ i for i in arr[1:] if i>pivot ]

        return quickSort(less) + [pivot] + quickSort(greater)



# --------------------------------------------------------
# bubbleSort
def  bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        flag = 0
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0: break
        
    return arr



# ---------------------------------------------------------
#  insertSort
def insertSort( arr ):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i] , arr[j] = arr[j], arr[i]
                
    return arr



# --------------------------------------------------------
# shell Sort
def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap>0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j>= gap and arr[j-gap]>temp:
                arr[j] = arr[j-gap]
                j = j - gap
            arr[j] = temp
        gap = round(gap/2)
    return arr

print (shellSort([5,4,3,2,1]) )
        




        





