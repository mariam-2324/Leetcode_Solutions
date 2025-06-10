class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # from typing import List
        """
        A class to find all possible permutations of a list of numbers.
        """
        """
        Generates all permutations of the input list 'nums'.

        Args:
            nums: A list of distinct integers.

        Returns:
            A list of lists, where each inner list is a unique permutation of 'nums'.
        """
        res = []  # This will store all the permutations
        visited = [False] * len(nums)  # To keep track of used numbers

        def backtrack(current_permutation: List[int]):
            """
            A recursive helper function to build permutations.
            """
            # Base case: If the current permutation is the same size as the input list,
            # we have found a complete permutation.
            if len(current_permutation) == len(nums):
                res.append(current_permutation[:])  # Add a copy to the results
                return

            # Iterate through all the numbers in the input list
            for i in range(len(nums)):
                # If the number at index 'i' has not been used yet
                if not visited[i]:
                    # 1. Choose: Add the number to our current permutation
                    current_permutation.append(nums[i])
                    visited[i] = True

                    # 2. Explore: Recurse with the updated permutation
                    backtrack(current_permutation)

                    # 3. Un-choose (Backtrack): Remove the number and reset its visited status
                    # to explore other possibilities.
                    current_permutation.pop()
                    visited[i] = False

        # Start the backtracking process with an empty permutation
        backtrack([])
        return res

# --- Example Usage ---
# Create an instance of the Solution class
solver = Solution()

# Define the input list
my_nums = [1, 2, 3]

# Get the permutations
permutations = solver.permute(my_nums)

# Print the result
print(f"Permutations for {my_nums}:")
print(permutations)
# Expected Output:
# Permutations for [1, 2, 3]:
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]