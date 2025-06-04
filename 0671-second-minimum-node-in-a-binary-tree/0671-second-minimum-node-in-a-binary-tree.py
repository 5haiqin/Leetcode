class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        vals = set()

        def dfs(node):
            if not node:
                return
            vals.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        vals = sorted(vals)
        return vals[1] if len(vals) > 1 else -1
