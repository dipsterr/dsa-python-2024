a = [10, 22, 12, 3, 0, 6]

def sor(a):
    n = len(a)
    arr= [a[-1]]
    currMax=a[-1]
    for i in range(-1, -n, -1):
        if(a[i] < a[i-1] and a[i-1]> currMax ):
            currMax= a[i-1]
            arr.append(a[i-1])
    return arr
        

        
print(sor(a))

