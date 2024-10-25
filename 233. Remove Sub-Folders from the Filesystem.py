from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.endOfFolder = False

    def add(self, path):
        cur = self
        for f in path.split("/"):
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        cur.endOfFolder = True

    def prefixSearch(self, path):
        cur = self
        folders = path.split("/")
        for i in range(len(folders)-1):
            cur = cur.children[folders[i]]
            if cur.endOfFolder:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()

        for f in folder:
            trie.add(f)
        res = []
        for f in folder:
            if not trie.prefixSearch(f):
                res.append(f)
        return res

if __name__ == "__main__":
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    print(Solution().removeSubfolders(folder))