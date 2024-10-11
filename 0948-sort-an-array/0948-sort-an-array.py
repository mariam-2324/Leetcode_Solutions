class Solution:
    def sortArray(self, nums):

        min_element = min(nums)
        max_element = max(nums)

        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1

        i = 0
        for num in range(min_element, max_element + 1):
            while count_map[num] > 0:
                nums[i] = num
                i += 1
                count_map[num] -= 1

        return nums