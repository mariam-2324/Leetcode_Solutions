class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq_map = {}
        max_freq = 0
        max_num = None

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
            if freq_map[num] > max_freq:
                max_freq = freq_map[num]
                max_num = num

        return max_num

