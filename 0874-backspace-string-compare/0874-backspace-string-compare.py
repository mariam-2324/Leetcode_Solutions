class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = b = ""
        for i in s:
            if i != '#':
                a += i
            else:
                a = a[:-1] 
        for i in t:
            if i != '#':
                b+=i
            else:
                b = b[:-1]
        return a == b 

        # strfirst = ''
        # count = 0
        # for i in range(len(s)):
        #     if (s[i] == '#'):
        #         count += 1
        #         continue
        #     if count > 0:
        #         count -= 1
        #     else:
        #         strfirst += s[i]
        # return True
        

