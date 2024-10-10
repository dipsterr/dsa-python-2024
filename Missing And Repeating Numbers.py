arr = [1,2,3,6,7,8,8,4,5]

def find(arr):

    sumarr = sum(set(arr))
    # return sumarr
    newarr = sum(range(1,len(arr)+1))
    miss = newarr-sumarr

    arr.sort()
    print(arr)
    
    tortoise = arr[0]
    hare = arr[0]

    while True:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
        if tortoise == hare:
            break

    tortoise = arr[0]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]
    
    return [hare, miss]

    

print(find(arr))

