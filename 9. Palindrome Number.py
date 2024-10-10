x = -123

# def palin(x):
#     x = str(x)
#     n = len(x)
#     for i in range (n//2):
#         if x[i]!=x[-1-i]:
#             return False   

#     return True

# print(palin(x))

str = 'Ab22Ba'
def palinCheck(str):
    i = 0
    j = len(str)-1
    while i<j:
        if str[i].isalnum() and str[j].isalnum():
            if str[i].lower() != str[j].lower():
                return False
            i+=1
            j-=1
        if not str[i].isalnum():
            i+=1
        if not str[j].isalnum():
            j-=1
    return True


print(palinCheck(str))
        

