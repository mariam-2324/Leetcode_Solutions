class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
    # def arrayRankTransform(self, arr):
        n = len(arr)  # Get the size of the input array
        
        if n == 0:    # If the array is empty, return an empty list
            return []
        
        # Get the unique elements in sorted order
        unique_elements = sorted(set(arr))
        # Create a dictionary to store the rank of each unique element
        # ranks = {ele: rank + 1 for rank, ele in enumerate(unique_elements)}
        ranks={ }
        rank=1
        for ele in unique_elements:
            ranks[ele]=rank
            rank+=1
        # Create the rank-transformed list by mapping each element to its rank
        # ans = [ranks[ele] for ele in arr]
        ans=[]
        for ele in arr:
            ans.append(ranks[ele])
        return ans  # Return the rank-transformed array