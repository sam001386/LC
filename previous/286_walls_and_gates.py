class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ### Naive BFS
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        from collections import deque
        queue = deque()
        seen = set()
        count = 1
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    seen.add((i, j))
        
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for direction in directions:
                    new_x = x + direction[0]
                    new_y = y + direction[1]
                    print(self.isvalid(new_x, new_y, rooms, seen))
                    if self.isvalid(new_x, new_y, rooms, seen):
                        queue.append((new_x, new_y))
                        seen.add((new_x, new_y))
                        rooms[new_x][new_y] = count
            count += 1
        
    def isvalid(self, new_x, new_y, rooms, seen):
        if new_x < 0 or new_x > len(rooms) - 1 or new_y < 0 or new_y > len(rooms[0]) - 1:
            return False
        elif rooms[new_x][new_y] == 0 or rooms[new_x][new_y] == -1:
            return False
        elif (new_x, new_y) in seen:
            return False
        return True
