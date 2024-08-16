class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count = {}
        for n in nums:
            if n in count:
                res += count[n]
                count[n] += 1
            else:
                count[n] = 1
        return res

#my 1st nested loop solutionO(n)^2
        # x = []
        # i, j = 0, 1
        # for i in range(len(nums)):
        #     for j in x:
        #         if nums[i] == nums[j] and nums[i] < nums[j]:
        #            x.append(j)
        #         elif nums[i] != nums[j]:

        # return x