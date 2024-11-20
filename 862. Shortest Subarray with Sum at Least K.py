nums = [1,2,4,3,5]

prefix = [0] * (len(nums)+1)

for i in range(1, len(nums)+1):
    prefix [i] = prefix [i-1] + nums[i-1]

print(prefix)
print(max(float("-inf"), 3))