class Solution(object):
    def integerReplacement(self, n):
        if n == 1:
            return 0
        queue = collections.deque()
        queue.append(n)
        res = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                if cur == 1:
                    return res
                elif cur % 2 == 0:
                    queue.append(cur // 2)
                else:
                    queue.append(cur + 1)
                    queue.append(cur - 1)
            res += 1 
        
        return res
                
