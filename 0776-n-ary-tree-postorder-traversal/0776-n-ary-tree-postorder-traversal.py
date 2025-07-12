
class Node:
    def __init__(self, val: int = None, children: list = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> list:
        if not root:
            return []

        res = []
        for child in root.children:
            res += self.postorder(child)
        res.append(root.val)
        return res
