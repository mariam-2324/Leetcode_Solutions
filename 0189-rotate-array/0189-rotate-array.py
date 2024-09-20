class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # Handle the case where k is greater than the length of the array
        nums.reverse()  # Reverse the entire array
    
    # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
    
    # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])