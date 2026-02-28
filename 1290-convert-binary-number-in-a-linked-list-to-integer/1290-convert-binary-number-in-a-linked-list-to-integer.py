class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        current = head
        
        while current:
            num = (num << 1) | current.val
            current = current.next
        
        return num