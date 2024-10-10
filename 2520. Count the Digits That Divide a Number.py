x = 121

def digit(x):
    res = 0
    for i in str(x):
        if x%int(i)==0:
            res+=1
    return res

print(digit(x))