class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx = 0 if ruleKey == "type" else 1 if ruleKey == "color" else 2
        
        cnt = 0
        for it in items:
            if it[idx] == ruleValue:
                cnt += 1
        return cnt
