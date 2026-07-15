# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        stack = [(root, root.val)]
        result = 0
        while stack:
            node, max_on_path = stack.pop()
            if node.val >= max_on_path:
                result += 1

            max_on_path = max(node.val, max_on_path)

            if node.right:
                stack.append((node.right, max_on_path))
            if node.left:
                stack.append((node.left, max_on_path))

        return result