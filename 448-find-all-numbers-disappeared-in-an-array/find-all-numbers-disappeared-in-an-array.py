class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # new = set(nums)
        # arr = []
        # for i in range(1, len(nums) + 1):
        #     if i not in new:
        #         arr.append(i)
                
        # return arr
        
        for n in nums:
            i = abs(n) - 1
            nums[i] = - 1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res

