class Solution:
    def isValid(self, s):
        stack = []
        pairs= {
            '(':')',
            '{':'}',
            '[':']'
        }

        for i in s:
            if i in pairs:
                stack.append(i)
            elif len(stack)==0 or i!= pairs[stack.pop()]:
                return False
        return len(stack)==0



if __name__ == "__main__":
    s = "(("
    print(type(s))
    print(Solution().isValid(s))
