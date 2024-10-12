num = 3172


def convert(num):
    res = []
    if num//1000:
        count = num//1000
        res.append(count*"M")
        num= num%1000

    if num//100:
        count = num//100
        if count <= 3:
            res.append(count*"C")
        elif 5 < count < 9:
            res.append("D"+(count-5)*"C")
        elif count == 5:
            res.append("D")
        elif count == 4:
            res.append("CD")
        elif count == 9:
            res.append("CM")
        num= num%100

    if num//10:
        count = num//10
        if count <= 3:
            res.append(count*"X")
        elif 5 < count < 9:
            res.append("L"+(count-5)*"X")
        elif count == 5:
            res.append("L")
        elif count == 4:
            res.append("XL")
        elif count == 9:
            res.append("XC")
        num= num%10

    
    if num <= 3:
        res.append(num*"I")
    elif 5 < num < 9:
        res.append("V"+(num-5)*"I")
    elif num == 5:
        res.append("V")
    elif num == 4:
        res.append("IV")
    elif num == 9:
        res.append("IX")


    res = ''.join(res)
    return res
      


print(154/426)