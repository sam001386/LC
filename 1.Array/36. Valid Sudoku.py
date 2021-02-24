class Solution(object):
    def isValidSudoku(self, A):
        for i in range(3):
            for j in range(3):
                seen = set()
                for r in range(i*3, i*3 + 3):
                    for c in range(j*3, j*3 + 3):
                        print(seen)
                        if A[r][c].isdigit() and A[r][c] not in seen:
                            seen.add(A[r][c])
                        elif A[r][c].isdigit():
                            return False 

        for r in range(9):
            seen = set()
            for c in range(9):
                if A[r][c].isdigit() and A[r][c] not in seen:
                        seen.add(A[r][c])
                elif A[r][c].isdigit():
                    return False 

        for c in range(9):
            seen = set()
            for r in range(9):
                if A[r][c].isdigit() and A[r][c] not in seen:
                    seen.add(A[r][c])
                elif A[r][c].isdigit():
                    return False
        
        return True
