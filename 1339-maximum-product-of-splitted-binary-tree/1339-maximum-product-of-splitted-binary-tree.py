class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.total = 0
        self.best = 0

        # Step 1: total sum
        def dfs1(node):
            if not node:
                return 0
            left = dfs1(node.left)
            right = dfs1(node.right)
            self.total += node.val
            return node.val + left + right

        dfs1(root)

        # Step 2: compute best split
        def dfs2(node):
            if not node:
                return 0
            left_sum = dfs2(node.left)
            right_sum = dfs2(node.right)
            subtree = node.val + left_sum + right_sum

            # candidate product
            self.best = max(self.best, subtree * (self.total - subtree))
            return subtree

        dfs2(root)

        return self.best % MOD
