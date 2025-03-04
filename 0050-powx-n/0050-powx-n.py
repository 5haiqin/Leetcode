class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: any number to power 0 is 1
        if n == 0:
            return 1
        
        # If power is negative, convert to positive and invert result
        if n < 0:
            x = 1 / x
            n = -n
        
        # Recursively compute power
        half = self.myPow(x, n // 2)
        
        # If power is even, multiply half by itself
        if n % 2 == 0:
            return half * half
        else:  # If power is odd, multiply extra x
            return half * half * x
