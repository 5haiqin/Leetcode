class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = [(root, root)]
        while q:
            a, b = q.pop(0)
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False
            q.append((a.left, b.right))
            q.append((a.right, b.left))
        return True
