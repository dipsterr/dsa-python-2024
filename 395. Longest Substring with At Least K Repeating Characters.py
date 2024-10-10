s = "aaabbcbb"
k = 2

from collections import Counter

def longest (s, k):

    length = len(s)
    if (k<=1):
        return length
    if (k>length or length ==0):
        return 0

    maxlength =  0
    counts = Counter(s)
    while maxlength < length and counts[s[maxlength]]>=k:
        maxlength+=1
    if maxlength >= length-1:
        return maxlength

    ls1 = longest(s[:maxlength], k)
    while maxlength < length and counts[s[maxlength]]<k:
        maxlength+=1
    ls2 = longest(s[maxlength:], k) if maxlength<length else 0
    return max(ls1, ls2)

print(longest (s, k))