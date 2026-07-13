# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def postorder_dfs(root: TreeNode | None) -> int:
            nonlocal diameter
            if root is None:
                return 0
            
            depths = {}
            stack = [(root, False)]
            while stack:
                node, visited = stack.pop()
                if not visited:
                    stack.append((node, True))
                    if node.left:
                        stack.append((node.left, False))
                    if node.right:
                        stack.append((node.right, False))
                else:
                    left_depth = depths.get(node.left, 0)
                    right_depth = depths.get(node.right, 0)

                    diameter = max(left_depth + right_depth, diameter)

                    depths[node] = max(left_depth, right_depth) + 1
            
            return depths[root]
            
        postorder_dfs(root)
        return diameter

        