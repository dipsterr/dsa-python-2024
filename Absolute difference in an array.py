
def absDiff(arr, n):
    even = 0
    odd  = 0
    for i in range(n):
        if i%2==0:
            even = abs(even-arr[i])
        else: 
            odd = abs(odd-arr[i])
    return even, odd
# def absDiff(arr, n):

    
#     evenStack = [arr[0]]
#     oddStack = [arr[1]]
#     for i in range (2,n):
#         if i%2==0:
#             value = arr[i]- evenStack.pop()
#             evenStack.append(value)
#         else:

#             value = arr[i]- oddStack.pop()
#             oddStack.append(value)
#     return evenStack.pop(), oddStack.pop()

print(absDiff([1, 2, 3, 4, 5, 6], 6))