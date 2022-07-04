# DFS approach

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
            
