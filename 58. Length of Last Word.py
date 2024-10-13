class Solution(object):
    def lengthOfLastWord(self, s):
        splitted = s.split()
        return len(splitted[-1])
        