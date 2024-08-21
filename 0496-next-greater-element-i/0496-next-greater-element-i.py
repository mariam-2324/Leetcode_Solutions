class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #set all array in enumerate(func)
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stk = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stk and cur > stk[-1]:
                val = stk.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stk.append(cur)
        return res
        
