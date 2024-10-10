from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int):
        res = nums
        i = 0
        
        while i < n :
            j = i+1
            while j<n:
                res.append(sum(nums[i:j+1]))
                j+=1
            i+=1
        return sum(sorted(nums)[left-1:right])

    

if __name__ == "__main__":
    nums = [1,2,3,4]
    res = Solution().rangeSum(nums, len(nums), 1, 5)
    print(res)