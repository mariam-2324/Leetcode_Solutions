class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_Dic = {}
        for i in nums:
            if i in my_Dic:
                return i
            else:
                my_Dic[i] = 1

