# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1
        def inorder_dfs(root: TreeNode | None):
            nonlocal count, k
            if root is None:
                return None

            left_result = inorder_dfs(root.left)
            if left_result is not None:
                return left_result 
            
            if count < k:
                count += 1
            else:
                return root.val

            right_result = inorder_dfs(root.right)
            if right_result is not None:
                return right_result

        return inorder_dfs(root)