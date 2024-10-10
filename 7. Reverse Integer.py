x = -123


def rev(x):
    res = 0
    n = x
    if x < -2147483648 or x>2147483648:
        return res
    elif x < 0:
        n = -(x)
    
    
    while (n>0):
        # rev = 
        res = res*10 + (n%10)
        n = n//10 
    if x < 0:
        return -res
    return res


print(rev(x))
