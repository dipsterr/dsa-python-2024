strs = ["cacecar","car"]
import sys

def prefix(strs):
    strs.sort()
    first = strs[0]
    last = strs[-1]
    res = ""
    for i in range(len(first)):
        if (first[0]!=last[0]):
            return -1
        elif(first[i]!=last[i]):
            return res
        else:
            res = res+first[i]
    return res

print(prefix(strs))
