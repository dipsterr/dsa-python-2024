class Solution(object):
    def minSteps(self, n):
        res = 0
        d = 2
        if n == 1:
            return 0

        while n > 1:
            while n%d==0:
                res += d
                n = n // d
            d+=1
        return res
            


