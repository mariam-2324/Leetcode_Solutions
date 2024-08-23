class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1, ans2 = set(), set()

        for n in nums1:
            if n not in nums2: 
               ans1.add(n)

        for n in nums2:
            if n not in nums1:
                ans2.add(n)

        return (ans1, ans2)
