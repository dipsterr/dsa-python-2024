class Solution:
    def isBalanced(self, num: str) -> bool:

        odd, even = [], []
        for i in range(len(num)):
            if i%2==0:
                even.append(int(num[i]))
            else:
                odd.append(int(num[i]))
        return sum(odd)==sum(even)


if __name__ == "__main__":
    num = "24123"
    print(Solution().isBalanced(num))
            
            
        