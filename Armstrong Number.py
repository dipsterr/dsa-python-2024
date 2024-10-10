num = 15

def arm(num):
    k = len(str(num))
    n = num
    armnum = 0
    while (n > 0):
        last = n%10
        armnum+=last**k
        n = n//10
    return num == armnum

print(arm(num))

