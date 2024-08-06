class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for i in range(0, len(gain)):
            temp = res[i] + gain[i]
            res.append(temp)
        return max(res)