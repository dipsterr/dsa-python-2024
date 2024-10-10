arr = [ 23,4,5,6,1]
import sys

def second(arr):
    smallest = sys.maxsize
    second = arr[0]
    for i in range(len(arr)):
        # smallest = min(second, smallest)
        if arr[i]<smallest:
            second = smallest
            smallest = arr[i]
        elif arr[i]>smallest and arr[i]<second:
            second = arr[i]   
    return second

print(second(arr))
# print(range(1,7))