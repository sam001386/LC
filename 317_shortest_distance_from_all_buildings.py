class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # check if we can reach all buildings
        # If similar number of empty land and buildings:
        # Time complexity: O(n ^ 4)
        # If empty land << buildings or empty land << buildings: 
        # Time complexity: O(n ^ 3)
        
        # Approach 1: search from the empty land
