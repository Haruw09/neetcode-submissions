# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i = 0
        j = 0
        elem_num = len(preorder)
        dummy = TreeNode(preorder[i])
        cur = dummy
        i += 1
        while j < elem_num:
            while i < elem_num and cur.val != inorder[j]:
                prev = cur
                cur.left = TreeNode(preorder[i])
                cur = cur.left
                cur.right = prev
                i += 1

            j += 1

            while j < elem_num and cur.right and inorder[j] == cur.right.val:
                prev = cur.right
                cur.right = None
                cur = prev
                j += 1

            if i < elem_num:
                prev = cur.right
                cur.right = TreeNode(preorder[i])
                cur = cur.right
                cur.right = prev
                i += 1

        return dummy
