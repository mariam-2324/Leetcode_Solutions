class Solution:
    def minOperations(self, nums, k):
        heapify(nums)
        res = 0

        while nums[0] < k:
            heappush(nums, 2*heappop(nums) + heappop(nums))
            res += 1

        return res
        