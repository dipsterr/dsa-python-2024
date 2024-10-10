s = "ababac"

from collections import Counter

# a = "a"
# print(s.count("a"))
def beautySum(s: str):
        # ans = 0 
        # for i in range(len(s)):
        #     freq = [0]*26
        #     for j in range(i, len(s)):
        #         freq[ord(s[j])-97] += 1
        #         print(ord(s[j])-97)
        #         ans += max(freq) - min(x for x in freq if x>0)
        # return ans 
    

    ans =0 
    for i in range(0,len(s)-1):
        mpp = {}
        for j in range(i,len(s)):
            if s[j] not in mpp:
                mpp[s[j]] = 1

                
            mpp[s[j]] +=1 

            maxx = max(mpp.values())
            minn = min(mpp.values())
            ans += maxx - minn 

    return ans 
    



        



print(beautySum(s))