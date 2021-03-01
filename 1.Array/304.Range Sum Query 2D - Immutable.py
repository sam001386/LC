class NumMatrix:

    def __init__(self, A: List[List[int]]):
        # Presum question
        if not A:
            return None
        presum = [[0 for _ in range(len(A[0]) + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(A[0]) + 1):
                presum[i][j] = presum[i - 1][j] + presum[i][j - 1] - presum[i - 1][j - 1] + A[i - 1][j - 1]
        self.presum = presum
        self.A = A

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        deltax = row2 - row1
        deltay = col2 - col1 
        return self.presum[row2 + 1][col2 + 1] - self.presum[row1][col2 + 1] - self.presum[row2 + 1][col1] + self.presum[row1][col1]
