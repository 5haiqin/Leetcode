from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head  # No rotation needed
        
        # Find the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length  # Handle cases where k >= length
        if k == 0:
            return head  # No rotation needed
        
        # Find the new tail (length - k - 1)th node
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # New head is next node
        new_head = new_tail.next
        new_tail.next = None  # Break the link
        tail.next = head  # Connect old tail to old head
        
        return new_head
