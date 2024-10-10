n = 4

for i in range (n, 0, -1):
    # for j in range(n, 0, -1):
    #     if (j>=i):
    #         print(j, end=" ")
    #     else:
    #         print(i, end=" ")
    for j in range(2, n+1):
        if (j>=i):
            print(j, end=" ")
        else:
            print(i, end=" ")

    print()

# for i in range(2, n+1):
#     for j in range(n, 0, -1):
#         if (j>=i):
#             print(j, end="")
#         else: 
#             print(i, end="")
#     for j in range(2, n+1):
#         if (j>=i):
#             print(j, end="")
#         else: 
#             print(i, end="")

#     print()   
# 

# for i in range(n, 0, -1):
#     for j in range(i, 1, -1):
#         print("_", end=" ")
#     for j in range(n, i-1, -1):
#         print(chr(64+j), end=" ")
#     print()

# for i in range(n):
#     for j in range(n, n-i-1, -1):
#         print(chr(64+j), end=" ")
#     print()

# for i in range(n):
#     for j in range(n):
#         if (i==0 or i == n-1 or j == 0 or j == n-1):
#             print(j, end="")
#         else:
#             print(" ", end="")
#     print()

     