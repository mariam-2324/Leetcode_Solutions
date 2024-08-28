class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        myset = Counter()
        maxl = 0
        while r < len(fruits):
            myset[fruits[r]] += 1
            r += 1
            if len(myset) <= 2:
                maxl = max(maxl, r - l)
            else:
                myset[fruits[l]] -= 1
                if myset[fruits[l]] == 0:
                    del myset[fruits[l]]
                l += 1
        return maxl







