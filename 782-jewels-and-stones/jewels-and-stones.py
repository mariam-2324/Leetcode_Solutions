class Solution:
    def numJewelsInStones(self, jewels_set: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels_set:
                count += 1
            
        return count