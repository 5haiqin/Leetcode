class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def proc(x):
            r = []
            for c in x:
                if c == '#':
                    if r:
                        r.pop()
                else:
                    r.append(c)
            return ''.join(r)
        return proc(s) == proc(t)
