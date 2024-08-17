class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapsT, mapTs = {}, {}
        c1, c2 = mapsT, mapTs

        for c1, c2 in zip(s,t):
            if ((c1 in mapsT and mapsT[c1] != c2) or
                (c2 in mapTs and mapTs[c2] != c1)):
                return False
            mapsT[c1] = c2
            mapTs[c2] = c1
        return True
        
        
         