class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        res = []
        for num in range(left, right + 1):
            if self.isSelfDividing(num):
                res.append(num)
        return res

    def isSelfDividing(self, num: int) -> bool:
        for digit in str(num):
            if digit == '0' or num % int(digit) != 0:
                return False
        return True
