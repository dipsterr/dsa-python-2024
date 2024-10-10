from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):
        index = 0
        for i in range(len(nums)):
            if nums[i]==0:
                i+=0
            else:
                nums[index], nums[i]= nums[i], 0
                index+=1
        


if __name__ == "__main__":
    nums = [0,1,0,3,12]

    Solution().moveZeroes(nums)
    print(nums)
    