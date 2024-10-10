
arr = []
from sys import maxsize
def pair(arr):
    sum = 0
    result = - maxsize

    if (len(arr)==1):
        return arr[0]
    elif (len(arr)==0):
        return 0

    for i in range (len(arr)-1):
        sum = arr[i]*arr[i+1]
        result = max(result, sum)
    return result

print(pair(arr))