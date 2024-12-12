from collections import Counter


class Solution(object):
    def takeCharacters(self, s, k):
        if len(s) < 3*k:
            return -1
        count = Counter(s)
        
        left = 0
        maxWindow = 0
        for right in range(len(s)):
            count[s[right]] -=1

            while min(count.values()) < k:

                count[s[left]] += 1
                left += 1 

            maxWindow = max(maxWindow, right - left + 1)

        return len(s)- maxWindow


if __name__ == "__main__":
    s = "abc"
    k = 1
    print(Solution().takeCharacters(s,k))


