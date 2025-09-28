from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = [0]*26
        for c in chars:
            cnt[ord(c) - ord('a')] += 1
        
        total = 0
        for w in words:
            wc = [0]*26
            ok = True
            for c in w:
                idx = ord(c) - ord('a')
                wc[idx] += 1
                if wc[idx] > cnt[idx]:
                    ok = False
                    break
            if ok:
                total += len(w)
        return total
