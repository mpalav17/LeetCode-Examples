class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        if len(s) == len(t):
            for i in range(0,len(s)):
                if s[i] in t:
                    t.pop(t.index(s[i]))
                else:
                    return False
            return True
        else:
            return False