s = ""

def rev(s):
    words = s.split()
    print(words)
    res = ""
    n = len(words)
    print(n)
    if (n <= 0):

        return res
    res= words[-1]
    for i in range (len(words)-2, -1, -1):
        res = res+"_"+words[i]
    return res

print(rev(s))