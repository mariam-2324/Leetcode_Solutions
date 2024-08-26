class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
    #   def maxScore(cardPoints, k):
        lsum = sum(cardPoints[:k])
        maxsum = lsum
        rsum = 0
        j = len(cardPoints) - 1
        for i in range(k - 1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[j]
            j -= 1
            maxsum = max(maxsum, lsum + rsum)
        return maxsum
