class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.total_tilt += abs(left - right)
            return node.val + left + right

        dfs(root)
        return self.total_tilt
