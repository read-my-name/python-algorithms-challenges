# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        # if not root:
        #     return []
        # queue = deque([root])
        # result = []
        # even = True
        # while queue:
        #     level_size = len(queue)
        #     current_level = deque([])
        #     for _ in range(level_size):
        #         node = queue.popleft()
        #         if even:
        #             current_level.append(node.val)
        #         else:
        #             current_level.appendleft(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     result.append(current_level)
        #     even = not even
        # return result
        if not root:
            return
        
        current = [root]
        is_left_right = True
        result = []
        while current:
            val, next_node = [], []
            for node in current:
                val.append(node.val)
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            if is_left_right:
                result.append(val)
            else:
                result.append(val[::-1])
            
            is_left_right = not is_left_right
            current = next_node

        return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(root))
        