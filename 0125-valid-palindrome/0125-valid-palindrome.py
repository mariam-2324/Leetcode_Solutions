class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        s2 = ''.join(c for c in s1 if c.isalnum())
        if s2 == s2[::-1]:
            return True
        else:
            return False

            