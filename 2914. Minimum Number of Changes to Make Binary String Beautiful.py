class Solution:
    def minChanges(self, s):
        count = 0
        for i in range(0,len(s),2):
            if s[i] != s[i+1]:
                count +=1
        return count
        
        
        pass

if __name__ == "__main__":
    s = "100110"
    print(Solution().minChanges(s))