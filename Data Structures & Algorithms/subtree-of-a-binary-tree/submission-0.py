# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def _is_same_tree(root_1: TreeNode | None, root_2: TreeNode | None) -> bool:
            if root_1 is None and root_2 is None:
                return True

            if root_1 is None or root_2 is None:
                return False

            return (
                root_1.val == root_2.val 
                and _is_same_tree(root_1.left, root_2.left)
                and _is_same_tree(root_1.right, root_2.right)
            )

        if root is None and subRoot is None:
            return True

        if root is None:
            return False

        if root.val == subRoot.val and _is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)