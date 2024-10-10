import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int):
        graph = collections.defaultdict(list)
        
        queue = collections.deque([root])
        
        while queue:
            
            node = queue.popleft()
            
            if node.left:
                graph[node.left.val].append((node.val, 'U'))
                graph[node.val].append((node.left.val, 'L'))

                queue.append(node.left)
            
            if node.right:
                graph[node.right.val].append((node.val, 'U'))
                graph[node.val].append((node.right.val, 'R'))

                queue.append(node.right)

        queue = collections.deque([(startValue, "")])  
        seen =  set ()

        while queue:

            current, path = queue.popleft()

            if current in seen:
                continue

            seen.add(current)

            if current == destValue:
                return path
            else:
                for child, direction in graph[current]:
                    if child not in seen:
                        queue.append((current, path+direction))
        pass