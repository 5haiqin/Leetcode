class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            l, d = e.split('@')
            l = l.split('+')[0].replace('.', '')
            s.add(l + '@' + d)
        return len(s)
