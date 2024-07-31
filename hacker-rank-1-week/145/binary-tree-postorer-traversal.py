
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
## 
## keep a stack of nodes
## if a node has been visited before pop it and add to the array
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res: list[int] = []
        stack: list[(TreeNode, bool)] = [(root, False)]
        while stack:
            cur, v = stack.pop()
            if cur is None:
                continue
            if v is True:
                res.append(cur.val)
            else:
                stack.append((cur, True))
                stack.append((cur.right, False))
                stack.append((cur.left, False))
        return res