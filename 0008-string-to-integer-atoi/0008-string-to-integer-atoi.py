class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Remove leading spaces
        s = s.lstrip()
        
        if not s:
            return 0  # If string is empty after removing spaces, return 0
        
        # Step 2: Check sign
        sign = 1  # Default sign is positive
        i = 0  # Pointer to traverse the string
        if s[i] == '-':
            sign = -1
            i += 1  # Move to the next character
        elif s[i] == '+':
            i += 1  # Just move to the next character
        
        # Step 3: Convert digits to integer
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])  # Build the number
            i += 1  # Move to the next character
        
        # Step 4: Apply sign
        result *= sign
        
        # Step 5: Clamp result within integer range (-2^31 to 2^31 - 1)
        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max
        
        return result
