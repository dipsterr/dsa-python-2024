from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int):
        k = len(nums)-k
        
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range (l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            nums[r], nums[p] = nums[p], nums[r]

            if p > k :
                return quickSelect(l, p-1)

            elif k > p :
                return quickSelect(p+1, r)

            else:
                return nums[p]
        

        return quickSelect(0, len(nums)-1)


if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print(Solution().findKthLargest(nums, k))