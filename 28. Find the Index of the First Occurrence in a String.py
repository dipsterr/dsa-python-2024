haystack = "stackhay"
needlle = "hau"

def fins(haystack, needlle):
    for i in range(len(haystack)):
        if haystack[i:i+len(needlle)]==needlle:
            return i
        else:
            continue
            

    return -1

print(fins(haystack, needlle))