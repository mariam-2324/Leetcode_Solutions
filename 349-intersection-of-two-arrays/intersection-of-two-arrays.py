class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = set(nums1)
        res = []
        for num in nums2:
            if num in hashmap and num not in res:
                res.append(num)

        return res