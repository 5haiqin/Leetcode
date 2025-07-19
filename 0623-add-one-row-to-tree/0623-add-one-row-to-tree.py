from collections import deque

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        q = deque([root])
        curr_depth = 1

        while q:
            if curr_depth == depth - 1:
                for node in q:
                    node.left = TreeNode(val, node.left)
                    node.right = TreeNode(val, None, node.right)
                return root

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            curr_depth += 1

        return root
