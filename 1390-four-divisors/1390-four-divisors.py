class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        
        for x in nums:
            count = 2
            summ = 1 + x
            i = 2
            
            while i * i <= x:
                if x % i == 0:
                    if i * i == x:
                        count += 1
                        summ += i
                    else:
                        count += 2
                        summ += i + x // i
                if count > 4:
                    break
                i += 1
            
            if count == 4:
                res += summ
        return res 