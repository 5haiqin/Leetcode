class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        ans = []
        mn, mx = 0, len(s)
        for c in s:
            if c == 'I':
                ans.append(mn)
                mn += 1
            else:
                ans.append(mx)
                mx -= 1
        ans.append(mn)
        return ans
