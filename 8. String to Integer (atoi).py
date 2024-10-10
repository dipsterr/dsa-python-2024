s = "+"

def atoi(s):
    st = s.strip()
    res = ""
    
    for i in st:
        
        if (i=="-" or  i=="+") and len(res)==0:
            res += i
        elif (i.isnumeric()):
            res +=i
        elif (i.isnumeric()==False and (len(res)==0 or res=="+" or res=="-")):
            return 0
        elif (i.isnumeric()==False):
            break
    # print(res)

    if (res=="-" or  res=="+"):
        return 0
    elif int(res)<0:
        # return 
        return max(-2**31, int(res))
    else:
        return min (2**31, int(res))
    # return int(res)

print((atoi(s)))






# print(int(+12))