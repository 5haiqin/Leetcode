from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        found_null = False

        while q:
            node = q.popleft()
            if not node:
                found_null = True
            else:
                if found_null:
                    return False
                q.append(node.left)
                q.append(node.right)
        
        return True
