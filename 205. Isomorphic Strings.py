
s = "bbbaaa"
t = "aaabbb"

def isomorphic(s, t):
    if (len(set(zip(s,t))))==len(set(s))==len(set(t)):
        return True
    return False

print(isomorphic(s, t))