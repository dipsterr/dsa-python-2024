def find(a):
    max = 0
    
    while a > 0:
        if a%10>max:
            max = a%10
        a = a//10
    
    return max

print(find(2845))