from typing import List
import heapq


class Solution:

    # def swap(self, nums, i, j):
    #     nums[i], nums[j] = nums[j], nums[i]
        
        
    # def shiftDown(self, nums, i, upper):
    #     while (True):
    #         l, r = i*2+1, i*2+2
    #         if max(l, r) < upper:
    #             if nums[i] >= max(nums[l], nums[r]):
    #                 break
    #             elif nums[l] > nums[r]:
    #                 Solution().swap(nums, i, l)
    #                 i = l
    #             else:
    #                 Solution().swap(nums, i, r)
    #                 i = r
    #         elif l < upper:
    #             if nums[l] > nums[i]:
    #                 Solution().swap(nums, i, l)
    #                 i = l
    #             else:
    #                 break
    #         elif r < upper:
    #             if nums[r] > nums[i]:
    #                 Solution().swap(nums, i, r)
    #                 i = r
    #             else: 
    #                 break
    #         else:
    #             break           
    
    # def sortArray(self, nums: List[int]):
    #     for i in range((len(nums)-2)//2, -1, -1):
    #         Solution().shiftDown(nums, i, len(nums))

    #     for end in range(len(nums)-1, 0, -1):
    #         Solution().swap(nums, 0, end)
    #         Solution().shiftDown(nums, 0, end)
    #     return nums
    def sortArray(self, nums: List[int]):
        heapq.heapify(nums)
        res = []

        while(nums):
            res.append(heapq.heappop(nums))
        return res
    
if __name__ == "__main__":
    nums = [5,2,3,1]
    res = Solution().sortArray(nums)
    print(res)