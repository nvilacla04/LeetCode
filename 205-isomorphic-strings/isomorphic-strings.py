class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import Counter
        
        s2t = {}
        t2s = {}

        for a,b in zip(s, t):
            if a in s2t and s2t[a] != b:
                return False

            if b in t2s and t2s[b] != a:
                return False

            s2t[a] = b
            t2s[b] = a
        return True 