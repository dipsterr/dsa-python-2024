s = "onnions"
from collections import Counter

def sortfreq(s):
    res = ""
    hashmap = Counter(s)
    lst = sorted(hashmap.items(), key = lambda x:-x[1])
    

    for key, value in lst:
        res = res+(key*value)

    return res
    

print(sortfreq(s))
