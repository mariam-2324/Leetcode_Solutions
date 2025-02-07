class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic={}

        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                return c