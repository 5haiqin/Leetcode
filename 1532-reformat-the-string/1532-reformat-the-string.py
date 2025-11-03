class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []
        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                letters.append(c)
        if abs(len(letters) - len(digits)) > 1:
            return ""
        # decide which list goes first
        turn_letters = len(letters) >= len(digits)
        res = []
        i = j = 0
        while i < len(letters) or j < len(digits):
            if turn_letters and i < len(letters):
                res.append(letters[i])
                i += 1
            elif not turn_letters and j < len(digits):
                res.append(digits[j])
                j += 1
            turn_letters = not turn_letters
        return "".join(res)
