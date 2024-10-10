from collections import Counter


def findX(arr):
    # write your code here
    count = Counter(arr)
    print(count)
    result = 0
    for key, value in count.items():
        if key==value:
            result = max(result, key)
    return result

print (findX([1, 2, 2, 3, 3, 3]))