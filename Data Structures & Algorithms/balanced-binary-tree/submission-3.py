# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: TreeNode | None) -> int:
            if not root:
                return 0
            heights = {None: 0}
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
                    if abs(heights[node.left] - heights[node.right]) > 1:
                        return -1

                    heights[node] = max(heights[node.left], heights[node.right]) + 1

            return heights[root]

        return height(root) != -1

