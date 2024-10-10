v =  [10,10,10,3,3,3]

def func(v):
    hashmap = dict()
    for i in v:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    
    minEle =min(hashmap.values())
    maxEle = max(hashmap.values())

    maxList = []    
    for key, value in hashmap.items():
        if value == maxEle:
            maxList.append(key)

    minList=[]
    for key, value in hashmap.items():
        if value == minEle:
            minList.append(key)
            # maxcount = value

    return maxList, minList

    
    freq_dict = dict()
    for i in v:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    
    max_val = max(freq_dict.values())
    min_val = min(freq_dict.values())
    
    max_list = []
    for i,j in freq_dict.items():
        if j == max_val:
            max_list.append(i)
    
    min_list = []
    for i,j in freq_dict.items():
        if j == min_val:
            min_list.append(i)
    
    return min(max_list),min(min_list)
print(func(v))