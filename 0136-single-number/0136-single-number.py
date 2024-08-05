class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        arr = []
        for i in nums:
            if i not in arr:
                arr.append(i)
            else:
                arr.remove(i)

        return arr[0]