s = "MCMXCIV"

def convert(s):
    res= 0
    for i in range(len(list(s))):
        if s[i]=="I":
            res+=1
        elif s[i]=="V" and i!=0 and s[i-1]=="I":
            res+=3
        elif s[i]=="V":
            res+=5
        elif s[i]=="X" and i!=0 and s[i-1]=="I":
            res+=8

        elif s[i]=="X":
            res+=10
        elif s[i]=="L" and i!=0 and s[i-1]=="X":
            res+=30
        elif s[i]=="L":
            res+=50
        elif s[i]=="C" and i!=0 and s[i-1]=="X":
            res+=80
        

        
        elif s[i]=="C":
            res+=100
        elif s[i]=="D" and i!=0 and s[i-1]=="C":
            res+=300
        elif s[i]=="D":
            res+=500
        elif s[i]=="M" and i!=0 and s[i-1]=="C":
            res+=800

        elif s[i]=="M":
            res+=1000
        
        


    return res

print(convert(s))