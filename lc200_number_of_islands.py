directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        seen = set()
        island_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == "1":
                    seen = self.bfs(i, j, grid, seen)
                    island_num += 1

        return island_num
    
    def bfs(self, i, j, grid, seen):
        queue = collections.deque()
        queue.append((i, j))
        size = 1
        while queue:
            r, c = queue.popleft()
            for direction in directions:
                x = direction[0] + r
                y = direction[1] + c
                if self.valid(x, y, grid, seen):
                    queue.append((x, y))
                    seen.add((x, y))
        return seen
    
    def valid(self, x, y, grid, seen):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        if grid[x][y] == "0":
            return False
        if (x, y) in seen:
            return False
        return True
