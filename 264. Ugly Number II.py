class Solution(object):
    def nthUglyNumber(self, n):
        nums = [1]
        i2, i3, i5 = 0, 0, 0
        while len(nums) < n:
            next_num = min(nums[i2] * 2, nums[i3] * 3, nums[i5]*5)
            nums.append(next_num)
            if next_num == nums[i2]*2:
                i2+=1
            if next_num == nums[i3]* 3:
                i3+=1
            if next_num == nums[i5]*5:
                i5+=1

        return nums[n-1]
    

if __name__ == "__main__":
    n= 11
    print(Solution().nthUglyNumber(n))
            
