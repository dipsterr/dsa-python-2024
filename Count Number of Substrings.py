s = "aba"

def countDistinctSubstrings(s, k):
    count = 0
    char_count = {}
    start = 0
    for i in range(len(s)):
        char_count[s[i]] = char_count.get(s[i], 0)+1

        while (len(char_count)>k):
            first = s[start]
            if (char_count[first]==1):
                del char_count[first]
            else:
                char_count[first] -=1
            start +=1
        
        count += (i - start+1)

    return count

def mainCode(s, k):
    return countDistinctSubstrings(s, k)


print(mainCode(s, 2))

# trie = Trie{}
