class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Convert both numbers to positive
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        
        # Subtract divisor from dividend using bit shifting
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple
        
        return sign * result
