class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = [0] * 26
        for c in magazine:
            cnt[ord(c) - ord('a')] += 1
        for c in ransomNote:
            i = ord(c) - ord('a')
            cnt[i] -= 1
            if cnt[i] < 0:
                return False
        return True
