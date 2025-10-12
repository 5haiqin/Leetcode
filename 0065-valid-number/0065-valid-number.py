class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        seenDigit = False
        seenDot = False
        seenE = False
        digitAfterE = True  

        for i, ch in enumerate(s):
            if ch.isdigit():
                seenDigit = True
                if seenE:
                    digitAfterE = True
            elif ch == '.':
                if seenDot or seenE:
                    return False
                seenDot = True
            elif ch == 'e' or ch == 'E':
                if seenE or not seenDigit:
                    return False
                seenE = True
                digitAfterE = False
            elif ch == '+' or ch == '-':
                if i != 0 and s[i-1] not in ('e', 'E'):
                    return False
            else:
                return False

        return seenDigit and digitAfterE
