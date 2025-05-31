class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return f"{root.val}({left})"
        
        return f"{root.val}({left})({right})"
