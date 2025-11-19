class Solution:
    def reformatNumber(self, number: str) -> str:
        s = ''.join(ch for ch in number if ch.isdigit())
        res = []
        i = 0
        n = len(s)
        while n - i > 4:
            res.append(s[i:i+3])
            i += 3
        rem = n - i
        if rem == 4:
            res.append(s[i:i+2])
            res.append(s[i+2:i+4])
        else:
            if rem > 0:
                res.append(s[i:])  # last 2 or 3 digits
        return '-'.join(res)
