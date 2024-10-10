s = "bbabbab"

def deletion(s):
    aCountRight = 0
    for a in s:
        aCountRight +=1 if a =="a" else 0
    
    bCountLeft = 0
    res = len(s)
    for char in s:
        if char == "a":
            aCountRight -= 1
        res = min(res, aCountRight + bCountLeft)
        if char == "b":
            bCountLeft +=1
    return res
    pass

print(deletion(s))