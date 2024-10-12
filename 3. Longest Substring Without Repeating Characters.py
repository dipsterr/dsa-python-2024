class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window={}
        sub_start = 0
        length = 0
        for sub_end in range(len(s)):
            char= s[sub_end]
            if char in  window and window[char]>= sub_start:
                sub_start= window[char]+1
            else:
                length= max(length, (sub_end-sub_start)+1)
            window[char]= sub_end
        
        return length