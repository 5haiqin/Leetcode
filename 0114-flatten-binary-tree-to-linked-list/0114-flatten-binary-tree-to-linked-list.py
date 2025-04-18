# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        temp = root.right
        root.right = root.left
        root.left = None
        
        cur = root
        while cur.right:
            cur = cur.right
        cur.right = temp
