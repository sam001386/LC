### Approach 1: Naive BFS
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seen = set()
        result = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in seen and board[row][col] == "O":
                    cur_list, seen = self.bfs(board, row, col, seen)
                    for cur in cur_list:
                        board[cur[0]][cur[1]] = "X"
    
    def bfs(self, board, x, y, seen):
        queue = collections.deque()
        queue.append((x, y))
        cur_list = [(x, y)]
        valid = 1
        while queue:
            cur_x, cur_y = queue.popleft()
            for direction in directions:
                new_x = direction[0] + cur_x
                new_y = direction[1] + cur_y
                if self.isvalid(new_x, new_y, board):
                    if (new_x, new_y) not in seen and board[new_x][new_y] == "O":
                        cur_list.append((new_x, new_y))
                        queue.append((new_x, new_y))
                        seen.add((new_x, new_y))
                else:
                    valid = 0
            
        if valid == 1:
            return cur_list, seen
        else:
            return [], seen

    def isvalid(self, x, y, board):
        if x < 0 or x > len(board)-1 or y < 0 or y > len(board[0])-1:
            return False
        return True
