

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
