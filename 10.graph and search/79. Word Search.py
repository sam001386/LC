directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def exist(self, A: List[List[str]], word: str) -> bool:
        if not A:
            return False
        seen = [[False for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == word[0]:
                    if self.dfs(i, j, A, word, 0, seen):
                        return True
        return False
    
    def dfs(self, i, j, A, word, index, seen):
        if i < 0 or i > len(A) - 1 or j < 0 or j > len(A[0]) - 1:
            return False
        elif A[i][j] != word[index]:
            return False
        elif seen[i][j] == True:
            return False
        if index == len(word) - 1:
            return True
        seen[i][j] = True
        res = self.dfs(i + 1, j, A, word, index + 1, seen) or\
        self.dfs(i - 1, j, A, word, index + 1, seen) or\
        self.dfs(i, j + 1, A, word, index + 1, seen) or\
        self.dfs(i, j - 1, A, word, index + 1, seen)
        seen[i][j] = False

        return res
