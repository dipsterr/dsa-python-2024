num = 30

def divisors(num):
    arr = [num]

    for i in range(num//2, 0, -1):
        if num%i==0:
            arr.append(i)
    return sorted(arr)

print(divisors(num))