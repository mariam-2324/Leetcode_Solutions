class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ""
        for i in range(len(s)):
            temp = indices.index(i)
            res = res + s[temp]
        return res
