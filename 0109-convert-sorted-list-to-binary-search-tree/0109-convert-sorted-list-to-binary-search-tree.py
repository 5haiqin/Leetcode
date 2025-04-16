# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def find_mid(start, end):
            slow = fast = start
            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            return slow

        def convert(start, end):
            if start == end:
                return None
            mid = find_mid(start, end)
            node = TreeNode(mid.val)
            node.left = convert(start, mid)
            node.right = convert(mid.next, end)
            return node

        return convert(head, None)
