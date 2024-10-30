class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        ans = 0
        i = 0         #left pointer
        j= len(nums) -1     #right pointer
        
        while i<j:
            if nums[i] + nums[j] == k:
                ans += 1 
                i += 1
                j -= 1
            elif nums[i] + nums[j] > k :
                
                j -= 1
                
            else:            # elif nums[i] + nums[j] < k:
                i += 1
                
        return ans