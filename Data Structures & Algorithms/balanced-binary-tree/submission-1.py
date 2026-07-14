# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balansed = True
        def dfs(root: TreeNode | None) -> int:
            nonlocal is_balansed
            if root is None:
                return 0

            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            depth = max(left_depth, right_depth) + 1

            is_balansed = (abs(left_depth - right_depth) <= 1) and is_balansed

            return depth

        dfs(root)
        return is_balansed