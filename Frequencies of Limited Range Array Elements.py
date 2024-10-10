
arr = [2, 3, 2, 3, 5]
N = 5
P = 5

def frequencyCount(arr, N, P):
    hashmap = {}
    for i in arr:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    for i in range(N):
        if (i+1) in hashmap:
            arr[i] = hashmap[i+1]
        else:
            arr[i]=0
        
    return arr


print(frequencyCount(arr, N, P))