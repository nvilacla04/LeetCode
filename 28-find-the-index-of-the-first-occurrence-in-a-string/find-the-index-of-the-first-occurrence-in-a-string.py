class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)

        #longest proper prefix 
        lps = [0]*m
        #length of current matched prefix 
        k = 0

        #if next char doesnt extend prefix fall back to next best shorter and try again
        for i in range(1, m):
            while k > 0 and needle[k] != needle[i]:
                k = lps[k-1]
            if needle[k] == needle[i]:
                k += 1
            lps[i] = k

        #scan the haystack on mismatch slide forward using lps 
        j = 0
        for i, ch in enumerate(haystack):
            while j > 0 and needle[j] != ch:
                j = lps[j-1]
            if needle[j] == ch:
                j += 1
            if j == m:
                return i - m + 1 

        return -1 

#O(m+n) approach