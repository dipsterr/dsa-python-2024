def remve(string):
    res = ""
    count = 0
    for i in string:

        # if (i=="("and count>0) or ( i==")"  and count>1):
        #     res = res+ i 

        if (i =="(" ):
            count+=1
        # elif (i==")" ):
        #     count-=1
        
            
    return count


string =  '1+(3*6+(9-3))'
print(remve(string))