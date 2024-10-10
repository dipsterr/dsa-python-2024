from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]):
        hashmap = dict()
        result = []
        for i in range(len(names)):
            hashmap[heights[i]] = names[i]
        for key in sorted(hashmap, reverse= True):
            result.append(hashmap[key])
        return result
            
            


if __name__ == "__main__":
    names = ["Mary","John","Emma"]
    heights = [180,165,170]
    res = Solution().sortPeople(names, heights)
    print(res)