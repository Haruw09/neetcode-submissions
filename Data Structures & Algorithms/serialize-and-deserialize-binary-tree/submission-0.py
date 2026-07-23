# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def dfs(node: TreeNode | None) -> None:
            nonlocal result
            if node is None:
                result.append('N')
                return None

            result.append(str(node.val) + '#')
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ''.join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        def dfs() -> TreeNode | None:
            nonlocal data, i
            if data[i] == 'N':
                i += 1
                return None

            cur_num = []
            while data[i] != '#':
                cur_num.append(data[i])
                i += 1

            i += 1
            cur_num = int(''.join(cur_num))

            cur = TreeNode(cur_num)
            cur.left = dfs()
            cur.right = dfs()

            return cur

        return dfs()
