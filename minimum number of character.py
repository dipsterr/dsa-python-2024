s = "abcabcded"

def removeMini(s):
    n = len(s)
    lis = [1]*n
    for i in range(1, n):
        for j in range(i):
            if s[i]> s[j]:
                lis[i] = max(lis[i], lis[j]+1)
    return n-max(lis)

print(removeMini(s))
