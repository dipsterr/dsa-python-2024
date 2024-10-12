class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        ans = []
        for r in range(numRows):
            skip = (numRows-1)*2
            for i in range(r, len(s), skip):
                ans.append(s[i])
                if ( r > 0 and r < numRows-1 and i+skip-2*r < len(s)):
                    ans.append(s[i+skip-2*r])
                    
        res = ''.join(ans)
        return res
    
if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))