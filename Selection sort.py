arr = [98,72,13,87,66,52,51,36]

def selectionsort(arr):
    for i in range(len(arr)-1):
        min = arr[i]
        for j in range(i, len(arr)):
            if (arr[j]<min):
                min = arr[j]
                arr[i], arr[j] = arr[j], arr[i]
    return arr



print(selectionsort(arr))