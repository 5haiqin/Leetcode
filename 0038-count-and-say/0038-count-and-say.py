class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)  # Get previous sequence
        result = ""
        count = 1  # Count occurrences
        
        for i in range(len(prev)):
            if i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1  # Increment count
            else:
                result += str(count) + prev[i]  # Append count and digit
                count = 1  # Reset count
        
        return result
