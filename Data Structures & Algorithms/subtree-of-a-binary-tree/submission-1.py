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

            stack = [(root_1, root_2)]
            while stack:
                node_1, node_2 = stack.pop()

                if node_1 is None and node_2 is None:
                    continue

                if node_1 is None or node_2 is None or node_1.val != node_2.val:
                    return False

                stack.append((node_1.right, node_2.right))
                stack.append((node_1.left, node_2.left))

            return True               

        if root is None and subRoot is None:
            return True

        if root is None:
            return False

        stack = [root]
        while stack:
            node = stack.pop()

            if _is_same_tree(node, subRoot):
                return True

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return False