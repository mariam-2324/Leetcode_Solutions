class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # num_set = set(nums)
        # n = len(nums) + 1
        # for i in range(n):
        #     if i not in num_set:
        #         return i

        #Optimized sol as per the problem's requirement.
         expected_sum = len(nums) * (len(nums) + 1) // 2
         actual_sum = sum(nums)
         return expected_sum - actual_sum 