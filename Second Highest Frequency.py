from collections import Counter

def secondHighest(nums):
    res = -1
    count = Counter(nums)
    firstMax, secondMax = 0, 0
    for key, value in count.items():
        # print(key, value)

        if value > firstMax :
            secondMax = firstMax
            firstMax = value
        elif firstMax > value and value > secondMax:
            secondMax = value
        
    for key, value in count.items():
        if value == secondMax:
            return key



nums = [1,1,2,2,3,3,3]
print(secondHighest(nums))