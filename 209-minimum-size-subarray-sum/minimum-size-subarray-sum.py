class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                current_length = r - l + 1
                res = min(res, current_length)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res
