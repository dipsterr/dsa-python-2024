
s = "abcba"
k = 6

import sys

def longest (s, k):
    i = 0
    j = 0
    hashmap = {}
    maxlength = -sys.maxsize

    while (j < len(s)):

        if s[j] not in hashmap:
            hashmap[s[j]]=1
        else:
            hashmap[s[j]]+=1
        
        if len(hashmap)==k or len(hashmap)<k:
            maxlength = max(maxlength, j-i+1)
        elif len(hashmap) > k:
            hashmap[s[i]] = hashmap[s[i]]-1
            if (hashmap[s[i]] == 0):
                hashmap.pop(s[i])
            i+=1
        j+=1

    return maxlength


print(longest(s, k))
