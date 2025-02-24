class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Convert strings to integers
        n1 = int(num1)
        n2 = int(num2)
        
        # Multiply the numbers
        result = n1 * n2
        
        # Convert back to string
        return str(result)
