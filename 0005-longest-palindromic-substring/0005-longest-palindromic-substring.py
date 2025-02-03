class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Extract the valid palindrome

        longest = ""
        for i in range(len(s)):
            # Check odd-length palindrome
            odd_palindrome = expandAroundCenter(i, i)
            # Check even-length palindrome
            even_palindrome = expandAroundCenter(i, i + 1)

            # Update longest palindrome found
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest
