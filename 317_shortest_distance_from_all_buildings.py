# Approach 1: search from the empty land
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # check if we can reach all buildings
        # If similar number of empty land and buildings:
        # Time complexity: O(n ^ 4)
        # If empty land << buildings or empty land << buildings: 
        # Time complexity: O(n ^ 3)
        # Idea: 1. do bfs (O(n^2)) for all "0" (O(n^2))
        #       2. compare the result and find the smallest one
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        num_1 = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = -1
                if grid[i][j] == 1:
                    num_1 += 1
        
        cur_result, result = 0, float("INF")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                new_grid = copy.deepcopy(grid)
                if grid[i][j] == 0:
                    cur_result = self.bfs(i, j, new_grid, num_1)
                    result = min(result, cur_result)
        return result if result != inf else -1
    
    def bfs(self, i, j, new_grid, num_1):
        queue = collections.deque()
        queue.append((i, j))
        seen = set()
        seen.add((i, j))
        cur_result = 0
        count = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for direction in directions:
                    x_new = x + direction[0]
                    y_new = y + direction[1]
                    if self.isvalid(x_new, y_new, new_grid, seen):
                        if new_grid[x_new][y_new] == 1:
                            cur_result += (count + 1)
                            seen.add((x_new, y_new))
                            num_1 -= 1
                        if new_grid[x_new][y_new] == 0:
                            queue.append((x_new, y_new))
                            seen.add((x_new, y_new))
                        elif new_grid[x_new][y_new] == 2:
                            seen.add((x_new, y_new))
            count += 1
        
        return cur_result if num_1 == 0 else float("INF")
    
    def isvalid(self, x, y, grid, seen):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        if (x, y) in seen:
            return False
        return True
