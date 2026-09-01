# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def pre_order(root):
            if not root:
                return
            
            root.left, root.right = root.right, root.left        
            pre_order(root.left)
            pre_order(root.right)

        pre_order(root)

        return root