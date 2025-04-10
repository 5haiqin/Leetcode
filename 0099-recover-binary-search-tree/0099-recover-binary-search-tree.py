# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        x = y = prev = None

        def inorder(node):
            nonlocal x, y, prev
            if not node:
                return
            inorder(node.left)
            if prev and node.val < prev.val:
                y = node
                if not x:
                    x = prev
                else:
                    return
            prev = node
            inorder(node.right)
        
        inorder(root)
        x.val, y.val = y.val, x.val
