class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
         ans = []
         for i in nums:#just start 1st loop and append the elements(i)in ans.
            ans.append(i)

         for n in nums:   #similarly,2nd loop again append nums elements  
            ans.append(n) # in ans array
         return ans     