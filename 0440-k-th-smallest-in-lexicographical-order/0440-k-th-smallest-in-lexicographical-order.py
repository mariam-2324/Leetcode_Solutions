class Solution:
    #def findKthNumber(self, n: int, k: int) -> int:
    def Count(self, curr, next, n):
        countNum = 0

        while curr <= n:
            countNum += (next - curr)
            curr *= 10
            next *= 10
            next = min(next, n + 1)

        return countNum

    def findKthNumber(self, n, k):
        curr = 1
        k -= 1  # Since we start from the first number (1), we need k-1 more numbers

        while k > 0:
            count = self.Count(curr, curr + 1, n)

            if count <= k:
                curr += 1
                k -= count  # skipping the elements under curr prefix tree
            else:
                curr *= 10
                k -= 1

        return curr