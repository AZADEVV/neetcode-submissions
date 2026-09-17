# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pre_i = 0
        in_i = 0

        def dfs(limit):
            nonlocal pre_i, in_i

            if pre_i >= len(preorder):
                return None
            if inorder[in_i] == limit:
                in_i += 1
                return None
            
            root = TreeNode(preorder[pre_i])
            pre_i += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        
        return dfs(float('inf'))
