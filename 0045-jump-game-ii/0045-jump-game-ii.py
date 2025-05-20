class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0           # Count of jumps
        current_end = 0     # End of the range for current jump
        farthest = 0        # Farthest index reachable in the current range

        for i in range(len(nums) - 1):  # No need to check the last element
            farthest = max(farthest, i + nums[i])  # Update farthest reachable index

            if i == current_end:  # If we reach the end of current jump range
                jumps += 1
                current_end = farthest  # Set new range to the farthest we can reach

        return jumps