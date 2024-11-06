from typing import List

class Solution:


    ans = []


    def recurPermute(self, index: int, nums: List[int], ans: List[List[int]]):
        if index == len(nums):
            ans.append(nums[:])
            return
        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.recurPermute(index + 1, nums, ans)
            nums[index], nums[i] = nums[i], nums[index]


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.recurPermute(0, nums, self.ans)
        return self.ans
    

    def isBalanced(self, num: str) -> bool:

        odd, even = [], []
        for i in range(len(num)):
            if i%2==0:
                even.append(int(num[i]))
            else:
                odd.append(int(num[i]))
        return sum(odd)==sum(even)


if __name__ == "__main__":

    v = "123"
    print(Solution().permute(v))
    # print(Solution().isBalanced(num))
            



