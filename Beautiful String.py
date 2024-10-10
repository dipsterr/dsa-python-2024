s = '01010010101'

def beautiful(string):
    res = 0
    s = list(string)
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            s[i] = str(int(s[i])^1)
            res+=1
    return res, s

print(beautiful(s))