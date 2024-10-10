nums = [1,2,4]
k = 5

def maxFrequency(nums, k):


    left, right, res, total = 0, 0, 0, 0

    length  = len(nums)

    while right < length:
        total += nums[right]

        while (nums[right]*(right -left + 1) > total+k):
            total -=nums[left]
            left +=1
        res = max(res, right-left+1)
        right +=1
    
    return res

    nums.sort()
    prev_op = 0
    freq = 1
    for i in range(1, len(nums)):
        prev_op += (nums[i] - nums[i-1])*freq
        if prev_op > k:
            prev_op -= (nums[i] - nums[i-freq])
        else:
            freq += 1
    return freq

    nums.sort()
    window_size, start, window_sum = 0, 0, 0

    for i in range(len(nums)):
        window_sum += nums[i]
        window_size += 1

        if (window_size - 1) * nums[i] + nums[i] > window_sum + k:
            window_sum -= nums[start]
            start += 1
            window_size -= 1

    return window_size

print(maxFrequency(nums, k))