class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i,nums in enumerate(sorted(nums)):
            if nums == target:
                arr.append(i)

        return arr
