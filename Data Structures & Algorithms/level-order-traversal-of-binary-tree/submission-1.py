# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        def depth(root):
            if not root: return 0
            return 1 + max(depth(root.left), depth(root.right))

        depth = depth(root)

        
        res = [[] for _ in range(depth)]
        
        queue = deque([root])
        level = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    res[level].append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)                
            level += 1
            

        return res


