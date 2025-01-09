class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sample = int(a, 2) + int(b, 2)
        return bin(sample)[2:]
