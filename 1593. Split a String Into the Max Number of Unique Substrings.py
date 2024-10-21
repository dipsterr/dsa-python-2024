class Solution(object):
    def maxUniqueSplit(self, s):
        def dfs(i, curr_set):
            if i == len(s):
                return 0

            res = 0
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if substr in curr_set:
                    continue
                curr_set.add(substr)
                res = max(res, 1+ dfs(j+1, curr_set))
                curr_set.remove(substr)
            return res
        
        return dfs(0, set())

if __name__ == "__main__":
    s = "ababccc"
    print(Solution().maxUniqueSplit(s))
        