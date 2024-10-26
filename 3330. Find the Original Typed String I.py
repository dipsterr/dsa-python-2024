from typing import List

class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                count +=1
                
        return count

    


if __name__ == "__main__":

    word = "abbcccc"


    print(Solution().possibleStringCount(word))