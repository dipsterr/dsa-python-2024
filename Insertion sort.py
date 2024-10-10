arr = [98,72,13,87,66,52,51,36]

def insertionsort(arr):
    n = len(arr)
    for i in range (1, n):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr



print(insertionsort(arr))