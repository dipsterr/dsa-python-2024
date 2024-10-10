s = "cabad"

def printSubStr(s, low, high):
    res = ""
    for i in range(low, high + 1):
        res+=s[i]
    return res

def longestPalindrome( s):
    n = len(s)
    start = 0
    end = 1

    for i in range (n):
        
        low = i-1
        hi = i

        while low >=0 and hi < n and s[low]==s[hi]:
            if hi - low +1 > end:
                start = low
                end = hi-low+1
            low-=1
            hi+=1


        low = i - 1
        hi = i + 1
 
        while low >= 0 and hi < n and s[low] == s[hi]:
            if hi - low + 1 > end:
                start = low
                end = hi - low + 1
            low -= 1
            hi += 1
    
    return printSubStr(s, start, start + end - 1)



print(longestPalindrome(s))