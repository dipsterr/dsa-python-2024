s = "68809"


def largeodd(num):
    n = len(num)
    for i in range(n-1, -1, -1):
        if int(num[i])%2!=0:
            return num[:i+1]
    return ""
        

    # while (i>0):
        
    #     if int(num)%2!=0:
    #         return num

    #     else:
    #         num = num[:i-1]
    #         if i==1:
    #             return ""
    #         i-=1

print((largeodd(s)))