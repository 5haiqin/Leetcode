from typing import Optional

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = None          # previous node value in inorder
        ans = float('inf')   # smallest difference found

        def inorder(node: Optional[TreeNode]):
            nonlocal prev, ans
            if not node:
                return
            inorder(node.left)
            if prev is not None:
                # update minimum difference
                diff = node.val - prev
                if diff < ans:
                    ans = diff
            prev = node.val
            inorder(node.right)

        inorder(root)
        return 0 if ans == float('inf') else int(ans)
