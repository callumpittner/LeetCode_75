class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x, y = 0, 0

        while x < len(s) and y < len(t):
            if s[x] == t[y]:
                x += 1
            y += 1

        return True if x == len(s) else False
    
