from typing import Optional, List

## ROOT --> LEFT --> RIGHT

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
         
## add to list the first time we visit 
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res: list[int] = []
        stack: list[(TreeNode, int)] = [(root, 0)]## bool tells us if its been added to res
        
        while stack:
            cur, v = stack.pop()
            if cur is None:
                continue
            if v == 0: ## first time visiting, so add to res
                res.append(cur.val) 
                stack.append(cur, 1)
                stack.append(cur.left, 0)
            if v == 1: ## we have visited it once, we need to go right
                stack.append(cur, 2)
                stack.append(cur.right, 0)
        return res