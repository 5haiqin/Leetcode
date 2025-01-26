class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Move slow pointer one step
            fast = fast.next.next      # Move fast pointer two steps
            
            if slow == fast:
                return True            # Cycle detected
        
        return False                   # No cycle found
