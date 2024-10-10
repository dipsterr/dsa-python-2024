s = "onionjonionionspl"
goal = "onions"

# s="clrwmpkru"
# goal = "wmpkruclr"

# if "c" in s:
#     print (s.index("c"))

def rotate(s, goal):
    # N = len(s)
    # if N != len(goal): return False
    # if N == 0: return True
    
    # shifts = [1]*(N+1)
    # left = -1
    # for right in range(N):
    #     while left >= 0 and goal[left] != goal[right]:
    #         left -= shifts[left]
    #     shifts[right + 1] = right - left
    #     left += 1
    # # return shifts
    # match_len = 0
    # for char in s+s:
    #     while match_len >= 0 and goal[match_len] != char:
    #         match_len -= shifts[match_len]

    #     match_len += 1
    #     if match_len == N:
    #         return True
    # return False
    return goal in s

    # return len(s) == len(goal) and s in goal+goal 

print(rotate(s, goal))

