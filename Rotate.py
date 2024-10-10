
# n=[-1, 0, 1, 1, -1, 0, 1, -1]
# k = 0
# # def longest(a, k):
# #     n = len(a)
# #     start = 0
# #     sum = a[0]
# #     max_length = 0

# #     for end in range(n):
        
# #         while (start <= end and sum > k):

# #             sum -= a[start]
# #             start += 1
        
# #         if (sum == k):
# #             max_length=max(max_length, (end-start)+1 )
        
# #         end +=1
# #         if (end<n):
# #             sum += a[end]

# #     return max_length
        


# # print(longest(n,k))


# def longest(a, k):
#     n = len(a)
#     sumMap = {}
#     max_length = 0
#     sum = 0

#     for i in range(n):
#         sum += a[i]

#         if (sum == k):
#             max_length = max(max_length, i+1)

#         rem = sum -k

#         if rem in sumMap:
#             length = i - sumMap[rem]
#             max_length = max(max_length, length)
        
#         if sum not in sumMap:
#             sumMap[sum] = i
        
#     return max_length
        


# print(longest(n,k))
        

        

    
# book = [1,2] 
# n = len(book)
# target = 1
# def read(n,book, target):
#     hashmap= {}
#     for i in range(n):
#         hashmap[book[i]] = i
#     for i in range(n):
#         if (target-book[i]) in hashmap and hashmap[target-book[i]]!=i:
#             return 'Yes'
#     return'No'

# print(read(n,book, target))


n=3



# for i in range(n):
#     for j in range(i+1):
#         print(chr(n+64-j), end=" ")
#     print()

# for i in range(n):
#     for j in range(n-i-1):

#         print(" ", end="")
#     print("*"*(2*i+1))

# for i in range(n):    
        
#     for j in range(2*n - (2*i)-2):
#             print(end=" ")
            
#     for j in range (i+1):
#         print(chr(j+65), end=" ")
    
#     for j in range(i-1, -1, -1):
#         print(chr(j+65), end=" ")

#     print()

for i in range(n):
    for j in range(i):
        print("*", end=" ")
    for j in range(2*n - (2*i)):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print("*", end=" ")

    print()

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")

    for j in range(2*n - (2*i)):
        print(" ",end=" ")

    for j in range(i, 0, -1):
        print("*", end=" ")

    print()
