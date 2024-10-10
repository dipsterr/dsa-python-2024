
s = "Test1ng-Leet=code-Q!"


def reverseOnlyLetters(s):
    n = len(s)
    i = 0
    j = n-1
    s= list(s)
    # print(s[i].isalpha())
    while (i<j):
        if (s[i].isalpha() and s[j].isalpha()):
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        if (not s[i].isalpha()):
            i+=1
        if (not s[j].isalpha()):
            j-=1
    return ''.join(s)

print (reverseOnlyLetters(s))

# print()




