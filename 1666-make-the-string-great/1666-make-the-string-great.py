class Solution:
    def makeGood(self, s: str) -> str:

        stk = []
        i = 0
        while i < len(s):
            if(
                stk and stk[-1] != s[i] and stk[-1].lower() == s[i].lower()):
                stk.pop()
            else:
                stk.append(s[i])
            i += 1
        return "".join(stk)


