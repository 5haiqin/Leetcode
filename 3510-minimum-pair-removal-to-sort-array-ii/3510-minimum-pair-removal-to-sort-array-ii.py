from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        prev = [i - 1 for i in range(n)]
        nxt = [i + 1 for i in range(n)]
        nxt[-1] = -1

        alive = [True] * n
        ver = [0] * n

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i, ver[i]))

        bad = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                bad += 1

        ops = 0

        while bad > 0:
            s, i, v = heapq.heappop(heap)
            j = nxt[i]

            if j == -1 or not alive[i] or not alive[j] or ver[i] != v:
                continue
            if nums[i] + nums[j] != s:
                continue

            a = prev[i]
            b = nxt[j]

            if a != -1 and alive[a] and nums[a] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if b != -1 and alive[b] and nums[j] > nums[b]:
                bad -= 1

            nums[i] = s
            alive[j] = False

            nxt[i] = b
            if b != -1:
                prev[b] = i

            ver[i] += 1
            ops += 1

            if a != -1 and alive[a] and nums[a] > nums[i]:
                bad += 1
            if b != -1 and alive[b] and nums[i] > nums[b]:
                bad += 1

            if a != -1 and alive[a]:
                heapq.heappush(heap, (nums[a] + nums[i], a, ver[a]))
            if b != -1 and alive[b]:
                heapq.heappush(heap, (nums[i] + nums[b], i, ver[i]))

        return ops
