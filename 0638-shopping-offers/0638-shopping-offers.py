class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        from functools import lru_cache

        n = len(price)

        @lru_cache(None)
        def dfs(curr_needs):
            res = sum(curr_needs[i] * price[i] for i in range(n))
            for offer in special:
                temp = list(curr_needs)
                for i in range(n):
                    if temp[i] < offer[i]:
                        break
                    temp[i] -= offer[i]
                else:
                    res = min(res, dfs(tuple(temp)) + offer[-1])
            return res

        return dfs(tuple(needs))
