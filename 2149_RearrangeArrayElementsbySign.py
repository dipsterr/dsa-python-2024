nums = [1,2,3,-4,-5,-6]

def func(nums):
    queue = []
    index = 0
    for i in range(len(nums)):

        if(index!=0 and nums[index-1] > 0 and nums[i] < 0 ):
            nums[index] = nums[i]
            index+=1
            if (len(queue)!=0):
                nums[index] = queue.pop(0)
                index+=1
            
        
        elif(index!=0 and nums[index-1] > 0 and nums[i]>0 ):
            queue.append(nums[i])

        elif(index!=0 and nums[index-1] < 0 and nums[i]<0 ):
            queue.append(nums[i])

        elif (nums[i] > 0):
            nums[index] = nums[i]
            index+=1
            if (len(queue)!=0):
                nums[index] = queue.pop(0)
                index+=1

        elif( nums[i] < 0):
            queue.append(nums[i])

    return nums


print(func(nums))