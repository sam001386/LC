class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # Union-find by ranking and path compression
        parent, rank = {}, {}
        def find(x):
            while parent[x] != x:
                parent[x] = x
            return parent[x]
        
        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0
            if rank[x] < rank[y]:
                x, y = y, x
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
            return 1
     
        counts, count = [], 0
        
        for i, j in positions:
            if (i, j) in parent:
                counts.append(count)
                continue
            x = parent[x] = i, j
            rank[x] = 0
            count += 1
            for y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if y in parent:
                    count -= union(x, y)
            counts.append(count)
            
        return counts

'''
###  Wrong approach ###
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        seen = set()
        island_num = []
        cur_island = 0
        for position in positions:
            count = 0
            for direction in directions:
                x = position[0] + direction[0]
                y = position[1] + direction[1]
                if self.valid(x, y, m, n) and (x, y) in seen:
                    seen.add(tuple(position))
                    island_num.append(cur_island)
                    break
                count += 1
            if count == 4:
                cur_island += 1
                island_num.append(cur_island)
                seen.add(tuple(position))
        return island_num
                    
        
    def valid(self, x, y, m, n):
        if x < 0 or x > m or y < 0 or y > m:
            return False
        return True
 
'''
