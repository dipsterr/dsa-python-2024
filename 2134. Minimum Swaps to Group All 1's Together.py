def minSwaps(nums):
    k = nums.count(1)
    maxSub = cnt = sum(nums[:k])
    n = len(nums)
    for i in range(k, n+k):
        cnt += nums[i%n]
        cnt -= nums[(i - k + n) % n]
        maxSub = max(maxSub, cnt)
    return k - maxSub


nums = [0,1,0,1,1,1,0]
print(minSwaps(nums))