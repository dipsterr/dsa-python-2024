class Solution:
    def minLength(self, s: str) -> int:

        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                if stack[-1]=='A' and char == 'B':
                    stack.pop()
                elif stack[-1]=='C' and char == 'D':
                    stack.pop()
                else:
                    stack.append(char)

        return len(stack)


if __name__ == "__main__":
    s = "ABFCACDB"

    print(Solution().minLength(s))