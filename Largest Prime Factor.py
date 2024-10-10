def largestPrimeFactor(n):
    # Write your code here
    result = -1
    i = 2
    while (i*i)<=n:
        while (n%i)==0:
            result = i
            n = n//i
        i+=1

    if n>1:
        return n

    return result

print(largestPrimeFactor(21))