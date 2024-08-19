class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        ind = 0
        while (i < len(t) and ind < len(s)):
            if (s[ind] == t[i]):
                 ind += 1
            i += 1
        if (ind == len(s)):
            return True
        else:
            return False
