# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, min_val, max_val):
            if not node:
                return True
            
            if (min_val is not None and node.val <= min_val) or (max_val is not None and node.val >= max_val):
                return False
            
            return is_valid(node.left, min_val, node.val) and is_valid(node.right, node.val, max_val)
        
        return is_valid(root, float('-inf'), float('inf'))
    
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(solution.isValidBST(root))
