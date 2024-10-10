s = "()(())()"
# print(len(s))

def maxDepth(vpsSeq, n):
    result = [0]* n
    flag = False
    ind = 0
    for i in vpsSeq:
        if i == "(":
            if (flag):
                result[ind]=1
                ind +=1
                flag = False
            else:
                flag = True
                ind +=1
        else:
            if (flag):
                flag = False
                ind +=1
            else:
                flag = True
                result[ind]=1
                ind+=1
    return result




print(maxDepth(s, len(s)))