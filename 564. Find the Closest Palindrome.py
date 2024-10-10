class Solution:
    def nearestPalindromic(self, n: str):
        num = int(n)
        i = 0
        j = len(n)-1
        
        while i<=j:
            if n[i]==n[j]:
                i+=1
                j-=1


        return
    


if __name__ == "__main__":
    n= "123"
    print(Solution().nearestPalindromic(n))