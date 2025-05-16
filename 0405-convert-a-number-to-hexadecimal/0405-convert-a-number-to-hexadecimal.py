class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        res = ""
        
        num &= 0xFFFFFFFF  # handle negative numbers
        
        while num > 0:
            res = hex_chars[num % 16] + res
            num //= 16
        
        return res
