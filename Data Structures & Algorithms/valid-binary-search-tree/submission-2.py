# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        stack = [(root, -float('inf'), float('inf'))]
        while stack:
            node, left_border, right_border = stack.pop()

            if node.val <= left_border or right_border <= node.val:
                return False
            
            if node.right:
                stack.append((node.right, node.val, right_border))
            if node.left:
                stack.append((node.left, left_border, node.val))

        return True
            