# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root: TreeNode | None) -> int:
            nonlocal diameter

            if root is None:
                return 0
            
            left_deapth = dfs(root.left)
            right_deapth = dfs(root.right)
            diameter = max(left_deapth + right_deapth, diameter)

            return max(left_deapth, right_deapth) + 1
            
        dfs(root)
        return diameter

        