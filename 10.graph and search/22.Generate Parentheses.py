# DFS recursive approach

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(paths, left, right):
            if right > left or left > n:
                return
            
            if len(paths) == n * 2:
                if left == right:
                    res.append(paths)
                return
            
            dfs(paths + "(", left + 1, right)
            dfs(paths + ")", left, right + 1)
        
        dfs("", 0, 0)
        
        return res
            
# BFS iterative approach

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = collections.deque()
        queue.append(["(", 1, 0])
        res = []
        while queue:
            cur, left, right = queue.popleft()
            if right > left or left > n or right > n:
                continue
            if left == right and len(cur) == 2 * n:
                res.append(cur)
            queue.append([cur + "(", left + 1, right])
            queue.append([cur + ")", left, right + 1])
            
        return res
            
