class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            jump = nums[i]  # get jump length at position i
            max_reach = max(max_reach, i + jump)
        return True