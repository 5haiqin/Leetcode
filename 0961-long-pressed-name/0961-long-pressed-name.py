class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        n, m = len(name), len(typed)
        
        while i < n and j < m:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        
        if i < n:
            return False
        
        while j < m:
            if typed[j] != typed[j-1]:
                return False
            j += 1
        
        return True
