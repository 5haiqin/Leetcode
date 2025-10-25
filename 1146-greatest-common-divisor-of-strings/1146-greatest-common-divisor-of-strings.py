class Solution:
    def gcdOfStrings(self, s: str, t: str) -> str:
        if s + t != t + s:
            return ""
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        g = gcd(len(s), len(t))
        return s[:g]
