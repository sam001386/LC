class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        st = [False for _ in range(10)]
        for i in range(n):
            fact = 1 
            for j in range(1, n - i):
                fact *= j 
            
            for j in range(1, n + 1):
                if st[j] == False:
                    if fact < k:
                        k -= fact 
                    else:
                        res += str(j)
                        st[j] = True 
                        break 
            
        return res
