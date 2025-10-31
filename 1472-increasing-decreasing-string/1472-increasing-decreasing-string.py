class Solution:
    def sortString(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        res = []
        n = len(s)
        while len(res) < n:
            for i in range(26):               
                if cnt[i]:
                    res.append(chr(i + 97))
                    cnt[i] -= 1
            for i in range(25, -1, -1):       
                if cnt[i]:
                    res.append(chr(i + 97))
                    cnt[i] -= 1
        return ''.join(res)
